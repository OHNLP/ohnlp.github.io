OHNLP Homepage
=============

The homepage of Open Health Natural Language Processing (OHNLP).

Install and Quick Start
-----------------------

The OHNLP homepage is built based on [Pelican](https://getpelican.com/), a Python-powered static site generator. You can install Pelican via several different methods. The simplest is via Pip and specify using markdown:

```bash
python -m pip install "pelican[markdown]"
```

Then, you can clone the repo and go to the root folder of the cloned repo:

```bash
pelican -r -l
```

The default local dev site will be served at `http://localhost:8000/`.
You can now open web browser and check the website for development.


Deployment
----------

To deploy the generated static site on GitHub Pages, the following steps should be followed:

1. Enable workflow permissions. In "Settings / Action / General", ensure the "Workflow permissions" is set to "Read and write permissions".
2. Enable GitHub Action and add a new workflow `main.yml`. 
   Copy the following content to create the workflow action. 
   It will take a few minutes to run. Once it shows completed without any error in the Action, you can move next step.
3. Enable the GitHub Pages. In "Settings / Pages", select:
    - Source: Deploy from a branch
    - Branch: gh-pages, /(root)

If everything works fine, you can find the `gh-pages` branch has been deployed on GitHub Pages and you can access it.

```yaml
# This is a basic workflow to help you get started with Actions

name: Deploy Latest Pages by Pelican

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "master" branch
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, Pelican!
          
      # Runs a build for pelican
      - name: GitHub Pages Pelican Build Action
        uses: nelsonjchen/gh-pages-pelican-action@0.1.10
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```


Settings
--------

Due to the special needs of hosting a static website, some settings in the `pelicanconf.py` have been customized to support our needs.

1. `*_SAVE_AS`. Some features are not used by a simple static website, such as author page, tag page, archive page, category page, etc. So, they are all disabled and removed from output list.


How to
------

How to update a page?
=====================


How to publish a news?
======================

You can publish a news by the following steps:

1. Create a new markdown file `.md` in the `/content/news` folder. Please just use simple file name,
2. Copy the following as the template and paste it at the begining
3. Commit the file and then GitHub Action script will try to convert the 