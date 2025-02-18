class MultiRegexURLResolver(urlresolvers.URLResolver):
    def __init__(self, urls, exceptions):
        super(MultiRegexURLResolver, self).__init__(RegexPattern(''), None)
        self._urls = urls
        self._exceptions = exceptions

    @property
    def url_patterns(self):
        return self._urls

    def resolve(self, path):
        tried = []
        matched = []
        patterns_matched = []

        # This is a simplified version of RegexURLResolver. It doesn't
        # support a regex prefix, and it doesn't need to handle include(),
        # so it's simplier, but otherwise this is mostly a copy/paste.
        for pattern in self.url_patterns:
            sub_match = pattern.resolve(path)
            if sub_match:
                # Here's the part that's different: instead of returning the
                # first match, build up a list of all matches.
                rm = urlresolvers.ResolverMatch(sub_match.func, sub_match.args, sub_match.kwargs, sub_match.url_name)
                matched.append(rm)
                patterns_matched.append([pattern])
            tried.append([pattern])
        if matched:
            return MultiResolverMatch(matched, self._exceptions, patterns_matched, path)
        raise urlresolvers.Resolver404({'tried': tried, 'path': path})
