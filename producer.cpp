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
#include <ndn-cxx/security/key-chain.hpp>
#include <ndn-cxx/security/signing-helpers.hpp>
//#include <ndn-cxx/lp/nack.hpp>
#include <iostream>
#include <list>

#define FAIL                                                                                                                                               \
  std::cerr << R"(usage: ./producer --prefix <perfix> --static </static/resource1> --static </static/resource2> --dynamic </dynamic/data1>)" << std::endl; \
  exit(1);

std::string prefix = "";
std::vector<std::string> staticNames;
std::vector<std::string> dynamicNames;

std::string genRandomString()
{
  std::string result;
  result.reserve(4096);
  for (int i = 0; i < 4096; i++)
  {
    result.push_back(random());
  }
  return result;
}

// Enclosing code in ndn simplifies coding (can also use `using namespace ndn`)
namespace ndn
{
  // Additional nested namespaces should be used to prevent/limit name conflicts
  namespace examples
  {

    class Producer
    {
    public:
      void
      run()
      {
        m_face.setInterestFilter(prefix,
                                 bind(&Producer::onFakeInterest, this, _1, _2),
                                 nullptr, // RegisterPrefixSuccessCallback is optional
                                 bind(&Producer::onRegisterFailed, this, _1, _2));

        for (const std::string &n : staticNames)
        {
          m_face.setInterestFilter(prefix + n,
                                   bind(&Producer::onStaticInterest, this, _1, _2),
                                   nullptr, // RegisterPrefixSuccessCallback is optional
                                   bind(&Producer::onRegisterFailed, this, _1, _2));
        }

        for (const std::string &n : dynamicNames)
        {
          m_face.setInterestFilter(prefix + n,
                                   bind(&Producer::onDynamicInterest, this, _1, _2),
                                   nullptr, // RegisterPrefixSuccessCallback is optional
                                   bind(&Producer::onRegisterFailed, this, _1, _2));
        }

        m_face.processEvents();
      }

    private:
      void
      onFakeInterest(const InterestFilter &, const Interest &interest)
      {
        std::cout << ">> I: " << interest << std::endl;
        // Create Data packet
        auto nack = make_shared<ndn::lp::Nack>(interest);
        auto &header = nack->getHeader();
        header.setReason(ndn::lp::NackReason::DDOS_FAKE_INTEREST);
        std::list<Name> names;
        names.push_back(Name("abdef"));
        names.push_back(Name("xyz1234"));
        names.push_back(Name("/example/testApp/randomData"));
        names.push_back(interest.getName());
        header.setNames(names);
        header.setPrefix(1);
        m_face.put(*nack);
      }

      void
      onStaticInterest(const InterestFilter &, const Interest &interest)
      {
        std::cout << ">> I: " << interest << std::endl;

        static const std::string content(genRandomString());

        // Create Data packet
        auto data = make_shared<Data>(interest.getName());
        data->setFreshnessPeriod(1000000_s);
        data->setContent(reinterpret_cast<const uint8_t *>(content.data()), content.size());
        data->setContentType(0);
        // Sign Data packet with default identity
        m_keyChain.sign(*data);

        // Return Data packet to the requester
        //std::cout << "<< D: " << *data << std::endl;
        m_face.put(*data);
      }

      void
      onDynamicInterest(const InterestFilter &, const Interest &interest)
      {
        std::cout << ">> I: " << interest << std::endl;

        static const std::string content(genRandomString());

        // Create Data packet
        auto data = make_shared<Data>(interest.getName());
        data->setFreshnessPeriod(2_s);
        data->setContent(reinterpret_cast<const uint8_t *>(content.data()), content.size());
        data->setContentType(0);
        // Sign Data packet with default identity
        m_keyChain.sign(*data);

        // Return Data packet to the requester
        //std::cout << "<< D: " << *data << std::endl;
        m_face.put(*data);
      }

      void
      onRegisterFailed(const Name &prefix, const std::string &reason)
      {
        std::cerr << "ERROR: Failed to register prefix '" << prefix
                  << "' with the local forwarder (" << reason << ")" << std::endl;
        m_face.shutdown();
      }

    private:
      Face m_face;
      KeyChain m_keyChain;
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
    else if (arg == "-s" || arg == "--static")
    {
      staticNames.push_back(argv[++i]);
    }
    else if (arg == "-d" || arg == "--dynamic")
    {
      dynamicNames.push_back(argv[++i]);
    }
    else
    {
      std::cerr << "unrecognized argument " << arg << std::endl;
      FAIL;
    }
  }

  try
  {
    ndn::examples::Producer producer;
    producer.run();
    return 0;
  }
  catch (const std::exception &e)
  {
    std::cerr << "ERROR: " << e.what() << std::endl;
    return 1;
  }
}
