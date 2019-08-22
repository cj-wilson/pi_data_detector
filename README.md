# Personal Information Detector

This repo contains a Jupyter notebook and python faker script to model detection of personally identifiable information.  It is a naive set of tools to determine the feasibility of detecting names, ssn's, addresses, and other personal information within random text.  Any data generated from this repo which may accidentally represent a person is the restult of the developer or data scientist and not this author.  No data is contained within this repo - it is generated from the Python faker library at https://faker.readthedocs.io/en/master/

## Background

The notebook used borrows *heavily* from the blog below.

https://www.depends-on-the-definition.com/guide-sequence-tagging-neural-networks-python/

It has been modified to use data generated from a faker script and not from a Kaggle data set.  The main difference is the handling of sentences as list pairs and not tuples.
