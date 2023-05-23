[![Python application](https://github.com/ObSob/hello-world-action/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/ObSob/hello-world-action/actions/workflows/main.yml)

# Hello world docker action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log.

## Inputs

## `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

## `time`

The time we greeted you.

## Example usage

uses: actions/hello-world-docker-action@v2
with:
  who-to-greet: 'Mona the Octocat'