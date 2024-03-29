    <script>
        /*
        @licstart  The following is the entire license notice for the
        JavaScript code in this page.

        Copyright (C) 2014-2017 GNUnet e.V.

        The JavaScript code in this page is free software: you can
        redistribute it and/or modify it under the terms of the GNU
        General Public License (GNU GPL) as published by the Free Software
        Foundation, either version 3 of the License, or (at your option)
        any later version.  The code is distributed WITHOUT ANY WARRANTY;
        without even the implied warranty of MERCHANTABILITY or FITNESS
        FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.

        As additional permission under GNU GPL version 3 section 7, you
        may distribute non-source (e.g., minimized or compacted) forms of
        that code without the copy of the GNU GPL normally required by
        section 4, provided you include this license notice and a URL
        through which recipients can access the Corresponding Source.

        @licend  The above is the entire license notice
        for the JavaScript code in this page.
        */
    </script>

    <link rel="alternate" hreflang="en" href="{{ self_localized('en') }}" />
    <link rel="alternate" hreflang="de" href="{{ self_localized('de') }}" />
    <link rel="alternate" hreflang="fr" href="{{ self_localized('fr') }}" />
    <link rel="alternate" hreflang="es" href="{{ self_localized('es') }}" />
    <link rel="alternate" hreflang="it" href="{{ self_localized('it') }}" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Contributors to the GNUnet website">
    <!--    <link rel="icon" href="../../favicon.ico"> -->

    <!-- Bootstrap core CSS -->
    <link href="{{ url_dist('css/bootstrap.min.css') }}" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="{{ url_static('styles.css') }}" rel="stylesheet">

    <script src="{{ url_dist('js/jquery-1.11.1.min.js') }}"></script>
    <script src="{{ url_dist('js/bootstrap.min.js') }}"></script>
    <link href="{{ url_static('navbar.css') }}" rel="stylesheet">

    <link href="{{ url_dist('font-awesome/css/all.css') }}" rel="stylesheet">

    <link href="{{ url_static('scroll.css') }}" rel="stylesheet">
    <script src="{{ url_static('scroll.js') }}"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <link rel="alternate" type="application/rss+xml" title="GNUnet.org rss" href="{{ url_localized('rss.xml') }}" />

    <!-- opengraph -->
    <!--
      We do not actively use Twitter or endorse it, but people might
      use our posts there or other websites might conform to the
      twitter namespace of the opengraph. More opengraph must be
      implemented in the sitecode.
      -->
    <meta name="twitter:card" content="article" />
    <meta name="twitter:site" content="@gnunet" />
    <meta name="twitter:creator" content="@gnunet" />
    {#
    TODO: Implement the necessary functions.
    <meta property="og:url" content="{{ url_localized(url) }}" />
    <meta property="og:title" content="{{ title }}" />
    <meta property="og:description" content="{{ summary }}" />
    <meta property="og:image" content="" />
    #}
