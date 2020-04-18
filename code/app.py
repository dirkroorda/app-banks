from tf.applib.helpers import dh
from tf.applib.api import setupApi
from tf.applib.links import outLink


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
    def __init__(*args, **kwargs):
        setupApi(*args, **kwargs)
        notice(args[0])

    def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
        api = app.api
        T = api.T

        (book, chapter, sentence) = T.sectionFromNode(n, fillup=True)
        passageText = app.sectionStrFromNode(n)
        href = "#" if _noUrl else app.docUrl
        if text is None:
            text = passageText
            title = f"show this passage online"
        else:
            title = passageText
        if _noUrl:
            title = None
        target = "" if _noUrl else None

        result = outLink(
            text,
            href,
            title=title,
            className=className,
            target=target,
            passage=passageText,
        )
        if _asString:
            return result
        dh(result)

    def fmt_layoutRich(app, n):
        api = app.api
        F = api.F
        after = f'{F.punc.v(n) or ""} '
        isGap = F.gap.v(n)
        material = F.letters.v(n) or ""
        layout = f'<span class="gap">{material}</span>' if isGap else material
        return f"{layout}{after}"
