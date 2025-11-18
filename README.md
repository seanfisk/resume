<!-- -*- coding: utf-8 -*- -->

# My Résumé

This is the source code for my résumé, written in LaTeX. It is built upon [tucv][], a résumé template.

## Setup

First, install [Homebrew][]. Then install all Homebrew dependencies using [Homebrew Bundle][]. This will install [MacTeX], a LaTeX distribution. This will take a long time.

    brew bundle install --verbose

## Building

Run:

    bin/build

The final PDF will be written to the `build/` directory.

## Testing

Run:

    bin/check

Checks will be performed and errors printed.

[Homebrew Bundle]: https://docs.brew.sh/Brew-Bundle-and-Brewfile
[Homebrew]: https://brew.sh/
[MacTeX]: https://www.tug.org/mactex/
[tucv]: http://www.ctan.org/pkg/tucv
