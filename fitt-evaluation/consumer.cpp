/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2013-2019 Regents of the University of California.
 *
 * This file is part of ndn-cxx library (NDN C++ library with eXperimental eXtensions).
 *
 * ndn-cxx library is free software: you can redistribute it and/or modify it under the
 * terms of the GNU Lesser General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later version.
 *
 * ndn-cxx library is distributed in the hope that it will be useful, but WITHOUT ANY
 * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
 * PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
 *
 * You should have received copies of the GNU General Public License and GNU Lesser
 * General Public License along with ndn-cxx, e.g., in COPYING.md file.  If not, see
 * <http://www.gnu.org/licenses/>.
 *
 * See AUTHORS.md for complete list of ndn-cxx authors and contributors.
 *
 * @author Alexander Afanasyev <http://lasr.cs.ucla.edu/afanasyev/index.html>
 */

#include <ndn-cxx/face.hpp>
#include <ndn-cxx/util/scheduler.hpp>

#include <boost/asio/io_service.hpp>
#include <iostream>

#define FAIL                                                                                                                \
  std::cerr << R"(usage: ./consumer --prefix <perfix> --name <name1> --name <name2> --period <milliseconds>)" << std::endl; \
  exit(1);

std::string prefix = "";
std::vector<std::string> names;
unsigned period = 500;

// Enclosing code in ndn simplifies coding (can also use `using namespace ndn`)
namespace ndn
{
  // Additional nested namespaces should be used to prevent/limit name conflicts
  namespace examples
  {

    class ConsumerWithTimer
    {
    public:
      ConsumerWithTimer()
          : m_face(m_ioService) // Create face with io_service object
            ,
            m_scheduler(m_ioService)
      {
      }

      void
      run()
      {
        m_scheduler.schedule(1_s, [this] { delayedInterest(); });
        m_ioService.run();
      }

    private:
      void
      onData(const Interest &, const Data &data) const
      {
        std::cout << "Received Data " << data << std::endl;
      }

      void
      onNack(const Interest &interest, const lp::Nack &nack) const
      {
        std::cout << "Received Nack with reason " << nack.getReason()
                  << " for " << interest << std::endl;
      }

      void
      onTimeout(const Interest &interest) const
      {
        std::cout << "Timeout for " << interest << std::endl;
      }

      void
      delayedInterest()
      {
        std::cout << "Sending Interest, delayed by the scheduler" << std::endl;

        for (const std::string &n : names)
        {
          Name interestName(prefix + n);
          //interestName.appendVersion();
          Interest interest(interestName);
          interest.setCanBePrefix(false);
          interest.setMustBeFresh(true);
          interest.setInterestLifetime(3_s);
          m_face.expressInterest(interest,
                                 bind(&ConsumerWithTimer::onData, this, _1, _2),
                                 bind(&ConsumerWithTimer::onNack, this, _1, _2),
                                 bind(&ConsumerWithTimer::onTimeout, this, _1));
        }
        m_scheduler.schedule(time::microseconds{period}, [this] { delayedInterest(); });
      }

    private:
      // Explicitly create io_service object, which will be shared between Face and Scheduler
      boost::asio::io_service m_ioService;
      Face m_face;
      Scheduler m_scheduler;
    };

  } // namespace examples
} // namespace ndn

int main(int argc, char **argv)
{
  if (argc == 1)
  {
    FAIL;
  }

  for (int i = 1; i < argc; i++)
  {
    std::string arg = argv[i];
    if (i == argc - 1)
    {
      std::cerr << "unrecognized argument " << arg << std::endl;
      FAIL;
    }
    if (arg == "-p" || arg == "--prefix")
    {
      prefix = (argv[++i]);
      std::cout << prefix;
    }
    else if (arg == "-n" || arg == "--name")
    {
      names.push_back(argv[++i]);
    }
    else if (arg == "--period")
    {
      period = atoi(argv[++i]);
    }
    else
    {
      std::cerr << "unrecognized argument " << arg << std::endl;
      FAIL;
    }
  }
  try
  {
    ndn::examples::ConsumerWithTimer consumer;
    consumer.run();
    return 0;
  }
  catch (const std::exception &e)
  {
    std::cerr << "ERROR: " << e.what() << std::endl;
    return 1;
  }
}
