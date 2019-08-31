from flask import _app_ctx_stack as stack, request
from werkzeug.local import LocalProxy

__all__ = ['Language', 'current_language']

def _current_language():
    ctx = stack.top

    if ctx is None:
        raise RuntimeError('Working outside of an application context.')

    return getattr(ctx, 'current_language', None)

current_language = LocalProxy(_current_language)

class Language(object):
    def __init__(self, app=None):
        self._allowed_languages = None
        self._default_language = None

        self.app = app
        if app is not None:
            self.init_app(app)

    def allowed_languages(self, callback):
        self._allowed_languages = callback
        return callback

    def default_language(self, callback):
        self._default_language = callback
        return callback

    def init_app(self, app):
        app.before_request(self.before_request)

    def before_request(self):
        ctx = stack.top
        accept_language_header = request.headers.get('Accept-Language', None)

        if accept_language_header:
            ctx.current_language = self._get_language(accept_language_header)
        else:
            ctx.current_language = self._default_language()

    def _get_language(self, accept_language_header):
        language = accept_language_header.split(',')[0]
        
        if language in self._allowed_languages():
            return language
        
        return self._default_language()


    @property
    def current_language(self):
        ctx = stack.top
        return ctx.current_language