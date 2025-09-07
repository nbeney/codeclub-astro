# [Astro](https://astro.build) GitHub Pages Template

## 🤖 Automatic Deployment to GitHub Pages

This minimal Astro project template comes with a [GitHub Action](https://github.com/features/actions) that automatically deploys your site to [GitHub Pages](https://pages.github.com/).

For more information, please see our complete deployment guide—[Deploy your Astro Site to GitHub Pages](https://docs.astro.build/en/guides/deploy/github/).

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

### Node.js/Astro Commands

| Command                | Action                                           |
| :--------------------- | :----------------------------------------------- |
| `npm install`          | Installs dependencies                            |
| `npm run dev`          | Starts local dev server at `localhost:3000`      |
| `npm run build`        | Build your production site to `./dist/`          |
| `npm run preview`      | Preview your build locally, before deploying     |
| `npm run astro ...`    | Run CLI commands like `astro add`, `astro check` |
| `npm run astro --help` | Get help using the Astro CLI                     |

### Python Commands

This project includes Python activities and solutions. The project is set up to use [uv](https://docs.astral.sh/uv/) for Python dependency management.

| Command                | Action                                           |
| :--------------------- | :----------------------------------------------- |
| `uv sync`              | Install Python dependencies                     |
| `uv run python <file>` | Run a Python file with project dependencies     |
| `uv run pytest`        | Run Python tests                                |
| `uv add <package>`     | Add a new Python dependency                     |

**Python Dependencies included:**
- `guizero` - For GUI applications
- `adventurelib` - For text adventure games  
- `pytest` - For testing

**Optional Graphics Dependencies:**
- `p5` - For p5.js-like graphics (available via `uv sync --extra graphics`, may require system dependencies)

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
