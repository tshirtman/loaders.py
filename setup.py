from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["pygame_loaders/*"]

setup(
        name = "pygame_loaders",
        version = "1.0",
        description = """
        a set of class/functions to use to load data in pygame
        applications, do memoization by default on data and on result of
        processings it allows on those datas
        """,
        author = "tshirtman",
        author_email = "gabriel.pettier@gmail.com",
        url = "http://github.com/tshirtman/loaders.py",
        # Name the folder where your packages live:
        # (If you have other packages (dirs) or
        # modules (py files) then
        # put them into the package directory -
        # they will be found 
        # recursively.)
        packages = ['pygame_loaders/'],
        # 'package' package must contain files (see list above)
        # I called the package 'package' thus cleverly confusing the whole
        # issue...
        # This dict maps the package name =to=> directories
        # It says, package *needs* these files.
        package_data = {'pygame_loaders' : 'pygame_loaders/' },
        # 'runner' is in the root.
        scripts = [],
        long_description = """
        This module was originaly a simple syntaxic sugar for a pygame project,
        for performances sake it quickly gained memoization, allowing you to
        call for images, not carring if you already loaded them or not. As you
        may need to do that for result of process on those images, the image
        loader gained a lot of keywords, that allow to call images with a
        zooms, blending, reversing, scaling, rotating, and all sort of
        combinations, everytime doing only the required parts of those
        processings, and using previous results of processings. Okay, it can
        takes up big memory amounts, but well, i found it's most of the time
        less of the problem than CPU, so if you agree, you will probably agree
        that for games, it's an acceptable tradeoff.

        Oh, for convenience sakes, it can load bunch of text and musics, too,
        the processing part is less developped on these ones, but contributions
        are welcomed, and memoization is done for them too.

        Anyway, using it is quite simple, simply import the needed loaders from
        loaders.py, and for an image filepath, image() will return a tupple
        containing the image and it's size, no need to store it away, calling
        the loader a second time or more is basically free, thanks to
        memoization.

        (assuming pygame is loaded!)
        >>> from pygame_loaders import image
        >>> image('myimage.png') # actual loading
        (<Surface(491x546x32 SW)>, <rect(0, 0, 491, 546)>)

        >>> image('myimage.png') # returning same result, without any loading
        >>> image("myimage.png", zoom=1.5) # only performing zoom
        (<Surface(736x819x32 SW)>, <rect(0, 0, 736, 819)>)

        >>> image("myimage.png", zoom=1.5, alpha=0.4) # only changing alpha
        (<Surface(736x819x32 SW)>, <rect(0, 0, 736, 819)>)

        """,
        # This next part it for the Cheese Shop, look a little down the page.
        classifiers = [])
