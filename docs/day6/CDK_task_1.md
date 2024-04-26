# AWS CDK Day 1

This document provides details about setting up AWS CDK for the iOLAP Academy assignments.

## Prerequisites

- Python [3.10.11](https://www.python.org/downloads/release/python-31011/) (64-bit)
- [Visual Studio Code](https://code.visualstudio.com/Download) (64-bit)
- Git [latest](https://git-scm.com/downloads) (64-bit)
- [AWS CLI v2](https://github.com/aws/aws-cli/tree/v2#installation)
- [Node.js](https://nodejs.org/en) (don't worry - we'll just use the package manager)
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install)

Update the repository with the following folder structure:

```
    └── cdk
```

## Getting started

For start, you will deploy a pre-made CDK stack.

1. Download and install all of the prerequisites
2. Copy materials (example_s3_stack folder) to your working directory which should be cdk/&lt;stack>
3. Activate the virtual environment
4. Install the dependencies via `pip install -r requirements.txt`
5. Change the stack name to include your name. E.g. "imijatovic-AcademyS3Stack". (app.py, line 10)
6. Try a `cdk synth`
7. Try a `cdk deploy`

## Task

Modify the CDK code so it creates 5 buckets instead of one, with numbered namings.
E.g. "imijatovic-academy-cdk-1", "imijatovic-academy-cdk-2"...

Hint: Python has loops.
