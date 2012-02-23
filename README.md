## DjangoCMS Embedded Pages

This simple extension allows your admin users to embed other pages within
placeholders

## Requirements

* django-cms
* And all the requirements the above project(s) depend on.


## Installation

1. make sure you are using a python virtual environment

     virtualenv ~/Dev/virtualenv/projectname;
     . ~/Dev/virtualenv/projectname/bin/activate;
     cd ~/Dev/projects/projectname/;

2. install it from pypi

    `pip install cmsplugin-embedded-pages`

3. or, install it from github

    `pip install git+https://github.com/airtonix/cmsplugin-embedded-pages`


## Configuration

1. add `cmsplugin_embeddedpages` to `INSTALLED_APPS`

2. perform a `./manage.py migrate` (for south users), or `./manage.py syncdb`

3. There is no step three!


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

* cmsplugin_embeddedpages/layouts

Any .html file that doesn't contain the word 'default' will be presented in
the template selector combo dropdown in the admin interface.

For example, if your django project was at :

    ~/Dev/Django/MyProjectName/

And you had a django application named `SomethingSomethingSomething` at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/

Then templates for this plugin could be found at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_embeddedpages/

In fact, anywhere django looks for templates, you can place the following tree :

    /cmsplugin_embeddedpages
        /layouts
            /groups
                /*.html
            /pages
                /*.html


### Customising Templates

All DjangoCMS plugin templates provided the context :

>     plugin' :
>         An instance of CMSPlugin, which itself provides reference to either
>         of the settings models as outlined below.

>     plugin.instance
>          An instance of the settings model unique to the plugin placed
>          in a placeholder.

>          group_template
>               Chosen template for groups of pages

>          page_template
>               Chosen template for singular pages.

>          include_root
>               boolean that is used to indicate whether or not to render
>               the root page content. This will always be False when the page
>               containing the placeholder in which this plugin is place is
>               the same as the root page.

>          depth
>               PositiveInteger that indicates how deep into the page hierachy
>               tree the plugin will traverse in order to seek pages for
>               embedding.

>          placeholders.all
>               ManyToMany field of page placeholders from which content will
>               be used for the output.


#### base.html

base.html in the `cmsplugin_configurableproduct` directory is used to load the
selected template chosen in the administration interface.

You should probably only touch this if you know what you are doing.


#### ./layouts/groups/*.html

Templates used to render a group of pages and are provided the context :

>     EmbeddedPages
>        A list of cms.Page(s) that match the settings of the plugin instance.


#### ./layouts/pages/*.html

Templates used to render individual pages.

Since templates here are used by the group template via `{% include %}` they
have all the same context variables as the group templates.

However in the default templates I provide, the page templates use the following:

>     EmbeddedPage
>        A single instance of a cms.Page


## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-embedded-pages


## Todo

provide option to manipulate menu choices:

* Refine the product filter.
* Provide better default templates.
* Allow selecting/use of snippets for menu templates?
