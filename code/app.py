from tf.applib.api import setupApi


def notice(app):
    if int(app.api.TF.version.split(".")[0]) <= 7:
        print(
            f"""
Your Text-Fabric is outdated.
It cannot load this version of the TF app `{app.appName}`.
Recommendation: upgrade Text-Fabric to version 8.
Hint:

    pip3 install --upgrade text-fabric

"""
        )


class TfApp(object):
    def __init__(app, *args, **kwargs):
        setupApi(app, *args, **kwargs)
        notice(app)

    def fmt_layoutRich(app, n):
        api = app.api
        F = api.F
        after = f'{F.punc.v(n) or ""} '
        isGap = F.gap.v(n)
        material = F.letters.v(n) or ""
        layout = f'<span class="gap">{material}</span>' if isGap else material
        return f"{layout}{after}"
