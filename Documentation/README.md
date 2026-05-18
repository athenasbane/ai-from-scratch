# AI From Scratch Documentation

This folder contains the documentation website. It is built with
[Docusaurus](https://docusaurus.io/), which is a tool for turning Markdown files
into a local website.

You do not need to know Node.js to edit the documents, but you do need Node.js
installed to preview the website on your computer.

## What You Need

- A terminal app:
  - macOS: Terminal, iTerm, or the terminal inside VS Code.
  - Windows: PowerShell, Windows Terminal, or the terminal inside VS Code.
  - Linux: your normal terminal.
- Node.js version 20 or newer.
- npm. This is installed automatically with Node.js.

## 1. Install Node.js

### macOS or Windows

1. Go to <https://nodejs.org/>.
2. Download the **LTS** version.
3. Run the installer.
4. Accept the default options.

After installing, close and reopen your terminal.

### Linux

Use your distribution's package manager, or install Node.js from
<https://nodejs.org/>.

This project needs Node.js `20` or newer.

## 2. Check Node.js Is Installed

Open a terminal and run:

```bash
node --version
```

You should see a version number such as:

```bash
v20.11.0
```

Then check npm:

```bash
npm --version
```

You should see another version number.

If `node` or `npm` is not found, restart your terminal and try again. If it still
does not work, reinstall Node.js from <https://nodejs.org/>.

## 3. Open The Project Folder

In your terminal, move into the documentation folder.

If you are already in the root of this repository:

```bash
cd Documentation
```

If you are somewhere else, use the full path to the project instead:

```bash
cd /path/to/ai-from-scratch/Documentation
```

For example, on this machine the path is:

```bash
cd /Users/beedge/Documents/projects.nosync/ai-from-scratch/Documentation
```

## 4. Install The Website Dependencies

Run this once before starting the website for the first time:

```bash
npm install
```

This downloads the tools listed in `package.json` into a local `node_modules`
folder. It can take a few minutes.

If the install succeeds, you can move to the next step.

## 5. Start The Documentation Website

From inside the `Documentation` folder, run:

```bash
npm run start
```

This starts a local development server. Docusaurus usually opens the website in
your browser automatically.

If it does not open automatically, go to:

```text
http://localhost:3000
```

Keep the terminal window open while you are working. The website runs from that
terminal process.

## 6. Edit Documents

The main documentation pages live in:

```text
docs/
```

For example:

```text
docs/types-of-learning.md
```

After saving a Markdown file, refresh the browser if the page does not update
automatically.

## 7. Stop The Website

Go back to the terminal running Docusaurus and press:

```text
Ctrl + C
```

That stops the local server.

## Build

To check that the full documentation site can be built for publishing, run:

```bash
npm run build
```

This creates a production version of the site in the `build` folder.

## Common Problems

### `node` command not found

Node.js is not installed, or your terminal has not picked it up yet.

Install Node.js from <https://nodejs.org/>, then close and reopen your terminal.

### `npm` command not found

npm should come with Node.js. Reinstall Node.js from <https://nodejs.org/>.

### `npm install` fails

Try these steps:

```bash
npm cache verify
npm install
```

If it still fails, check that your internet connection is working and that you
are inside the `Documentation` folder.

### Port `3000` is already in use

Something else is already using the default Docusaurus port.

Run:

```bash
npm run start -- --port 3001
```

Then open:

```text
http://localhost:3001
```

### Math Or LaTeX Does Not Render

This site uses KaTeX through Docusaurus. If math such as `$x_i$` or `$$x^2$$`
does not render, make sure dependencies are installed:

```bash
npm install
```

Then restart the local server:

```bash
npm run start
```

## Useful Commands

Run these commands from inside the `Documentation` folder.

Start the local website:

```bash
npm run start
```

Build the production website:

```bash
npm run build
```

Run TypeScript checks:

```bash
npm run typecheck
```
