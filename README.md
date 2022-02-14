# docker-adder

Simple command-line adder function to practice docker

## GOALS

- Dockerize a program that takes 2 numbers via user CLI and returns the sum of
  those numbers.
- The program should be developed with tests using a simple CI/CD pipeline.

## INSTALLATION:

- clone repo to local machine.
- launch docker desktop.
- `docker build --tag docker-adder .`
- `docker run docker-adder`

## NOTES:

### CI/CD Options:

- CircleCI: https://circleci.com/blog/build-cicd-piplines-using-docker/
- GitHub Actions described by Docker:
  https://docs.docker.com/language/python/configure-ci-cd/
