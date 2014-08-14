# Mountain

[Fountain](http://fountain.io) is a plain-text markup language for
screenwriting.

Fountain is awesome, but it can be somewhat cumbersome to use in practice
because the vast majority of [Fountain apps](http://fountain.io/apps) assume
that the entire screenplay is housed in a single file.

This means that if you're storing your screenplay in multiple files (say, a
file per scene or sequence), then you're likely fighting an uphill battle
against your screenwriting software.

This isn't Fountain's fault -- it's just a markup language, and file
organization is a higher-level concern.

That being said, we can change the equation by building tooling (see
[exhibit A](http://johnaugust.com/2014/fountain-for-coders-or-the-joy-of-writing)
and [exhibit B](http://slugline.co/blog/shotlists) for examples unrelated to
the concern of file organization).

Mountain makes it possible to arbitrarily organize the file layout of your
screenplay. More specifically, it is a tool for intelligently splitting and
combining files in the Fountain screenplay format\*.

See the accompanying
[blog post](http://blog.mjrusso.com/2014/08/15/mountain-screenwriting-with-fountain.html)
for more details on the specific motivations that led to this tool's creation,
and why multi-file screenplays may be beneficial to your screenwriting
workflow.

_\* Technically, there's not really anything in Mountain that's
Fountain-specific, besides the usage of the notes syntax (`[[ ]]`) to specify
**directives**. However, it was built specifically to make working with long
Fountain documents more palatable._

## Installation

```bash
git clone https://github.com/mjrusso/mountain.git
cd mountain
python setup.py install
```

After installation, the `mountain` binary will be available in your `$PATH`.

Note that Python >= 2.7 is required to run this project.

## Usage

The following command will print detailed usage information:

```bash
mountain --help
```

There are two main commands available -- `mountain join`, and `mountain split`.

### Tutorial

Create an outline file (or "manifest"). We'll call the file `manifest.fountain`
for the purpose of this tutorial, but it can be named whatever you like.

_manifest.fountain_:

```markdown
# ACT I

= Meet the **Hero**.

[[#include intro.fountain]]

# ACT II

# ACT III

## Finale

[[#include the-end.fountain]]
```

This file probably looks like a lot like how most Fountain screenplays start,
with the exception of the two notes that begin with `#include`.

Here, `#include` is a **directive** that points to another file that should be
included in its place.

_intro.fountain_:

```markdown
FADE IN:
```

_the-end.fountain_:

```markdown
> FADE OUT.

>THE END<
```

This is the shell of our screenplay.

To produce a single document from these disparate files, execute the following
command:

```bash
mountain join manifest.fountain screenplay.fountain
```

This will result in the creation of _screenplay.fountain_.

_screenplay.fountain_:

```markdown
# ACT I

= Meet the **Hero**.

[[#reference intro.fountain]]

FADE IN:

[[/reference]]

# ACT II

# ACT III

## Finale

[[#reference the-end.fountain]]

> FADE OUT.

>THE END<

[[/reference]]
```

This new document is a combination of _manifest.fountain_ and each of the files
referenced in the manifest (_intro.fountain_, _the-end.fountain_). These
referenced files are included in-line and wrapped in the `#reference ...
/reference` directive.

Mountain works in both directions. To see this in action, edit the combined
document (_screenplay.fountain_), so that it looks like this:

_screenplay.fountain_:

```markdown
# ACT I

= Meet the **Hero**.

## The World

[[#reference intro.fountain]]

FADE IN:

A green, open field, stretching for miles in all directions.

[[/reference]]

# ACT II

# ACT III

## Finale

[[#reference the-end.fountain]]

> FADE OUT.

>THE END<

[[/reference]]
```

At this point, the combined document (_screenplay.fountain_) is the source of
truth, as it has information that isn't in a few of the other documents.

To update the other documents (i.e., the manifest and each of the files it
references), execute the following command:

```bash
mountain split manifest.fountain screenplay.fountain
```

As with `mountain join`, the first argument is the path to the manifest file, and the
second argument is the path to the combined document.

After running this command, _manifest.fountain_ and _intro.fountain_ will
update to reflect the changes (adding a new section header, and a line of
action description, respectively). When we edited _screenplay.fountain_ we
didn't make any changes to _the-end.fountain_, so there won't be any visible
changes to that file.

_manifest.fountain_:

```markdown
# ACT I

= Meet the **Hero**.

## The World

[[#include intro.fountain]]

# ACT II

# ACT III

## Finale

[[#include the-end.fountain]]
```

_intro.fountain_:

```markdown
FADE IN:

A green, open field, stretching for miles in all directions.
```

Because this works bi-directionally, you can continue to run the `join` and
`split` commands in any sequence you wish (just remember to keep track of what
document(s) are the "source of truth", or you may inadvertently lose some work
-- Mountain overwrites files). Keep in mind that in most workflows, you won't
be frequently jumping back and forth between these two modes.

### Additional Notes

- Use a relative file path in an `#include` directive (relative to the
  directory that the manifest file is located in). For example, if you write
  `[[#include a.fountain]]`, then _a.fountain_ should be in the same folder as
  the manifest file.

- Referenced files can be in different folders. For example,
  `[[#include act iii/the-end.fountain]]` is legal (_the-end.fountain_ should
  be located within a folder called _act iii_, relative to
  _manifest.fountain_'s directory).

- Mountain works with any file extension, not just _.fountain_.

- If a file that does not exist is referenced in an `#include` directive, and
  the `mountain join` command is executed, then the `#include` directive will
  remain in the resultant combined document. (It will not be converted to
  `#reference ... \reference`, and an error will not be thrown.)

- Mountain does not support recursive includes (i.e., a file that is included
  via `#include` can't itself include another file via `#include`).

## Development

Mountain can be run without installing it first (useful when developing) in one
of the following two ways:

```bash
./run.py --help
```

```bash
python -m mountain --help
```

(Either of these commands must be run from the root of this project's
directory.)

### Tests

To execute the tests, run the following command:

```bash
python setup.py test
```

The tests use fixtures located at `./test/fixtures/`.

## Copyright

Copyright (c) 2014 [Michael Russo](http://mjrusso.com). See LICENSE for details.
