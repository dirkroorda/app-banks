from tf.core.helpers import mdhtmlEsc, htmlEsc
from tf.applib.helpers import dh
from tf.applib.display import prettyPre, getFeatures
from tf.applib.highlight import hlText, hlRep
from tf.applib.api import setupApi
from tf.applib.links import outLink

SECTION = {'book', 'chapter', 'sentence'}


class TfApp(object):

  def __init__(*args, **kwargs):
    setupApi(*args, **kwargs)

  def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
    api = app.api
    T = api.T

    (book, chapter, sentence) = T.sectionFromNode(n, fillup=True)
    passageText = app.sectionStrFromNode(n)
    href = '#' if _noUrl else app.docUrl
    if text is None:
      text = passageText
      title = f'show this passage online'
    else:
      title = passageText
    if _noUrl:
      title = None
    target = '' if _noUrl else None

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
    material = F.letters.v(n) or ''
    layout = f'<span class="gap">{material}</span>' if isGap else material
    return f'{layout}{after}'

  def _plain(
      app,
      n,
      passage,
      isLinked,
      _asString,
      secLabel,
      **options,
  ):
    display = app.display
    d = display.get(options)

    _asApp = app._asApp
    api = app.api
    F = api.F
    L = api.L
    T = api.T

    nType = F.otype.v(n)
    result = passage
    if _asApp:
      nodeRep = f' <a href="#" class="nd">{n}</a> ' if d.withNodes else ''
    else:
      nodeRep = f' <i>{n}</i> ' if d.withNodes else ''

    rep = ''
    text = ''
    if nType == 'word':
      text = hlText(app, [n], d.highlights, fmt=d.fmt)
    elif nType in {'line', 'sentence'}:
      text = hlText(app, L.d(n, otype='word'), d.highlights, fmt=d.fmt)
    elif nType in SECTION:
      if secLabel and d.withPassage:
        sep1 = app.sectionSep1
        sep2 = app.sectionSep2
        label = (
            '{}'
            if nType == 'book' else
            f'{{}}{sep1}{{}}' if nType == 'chapter' else
            f'{{}}{sep1}{{}}{sep2}{{}}'
        )
        rep = label.format(*T.sectionFromNode(n))
        rep = mdhtmlEsc(rep)
        rep = hlRep(app, rep, n, d.highlights)
        if isLinked:
          rep = app.webLink(n, text=f'{rep}&nbsp;', _asString=True)
      else:
        rep = ''
      if nType == 'sentence':
        rep += mdhtmlEsc(f'{nType} {F.number.v(n)}') if secLabel else ''
      elif nType == 'chapter':
        rep += mdhtmlEsc(f'{nType} {F.number.v(n)}') if secLabel else ''
      elif nType == 'book':
        rep += mdhtmlEsc(f'{nType} {F.title.v(n)}') if secLabel else ''
      rep = hlRep(app, rep, n, d.highlights)
      if text:
        text = hlRep(app, text, n, d.highlights)
    else:
      rep = hlText(app, L.d(n, otype='word'), d.highlights, fmt=d.fmt)
    if text:
      tClass = display.formatClass[d.fmt].lower()
      text = f'<span class="{tClass}">{text}</span>'
      rep += text
    rep = app._addLink(
        n,
        rep,
        nodeRep,
        isLinked=isLinked and nType not in SECTION,
    )
    result += rep

    if _asString or _asApp:
      return result
    dh(result)

  def _addLink(app, n, rep, nodeRep, isLinked=None):
    if isLinked:
      rep = app.webLink(n, text=rep, _asString=True)
    theLine = ''
    return f'{rep}{nodeRep}{theLine}'

  def _pretty(
      app,
      n,
      outer,
      html,
      firstSlot,
      lastSlot,
      **options,
  ):
    display = app.display
    d = display.get(options)

    goOn = prettyPre(
        app,
        n,
        firstSlot,
        lastSlot,
        d.withNodes,
        d.highlights,
    )
    if not goOn:
      return
    (
        slotType,
        nType,
        className,
        boundaryClass,
        hlAtt,
        nodePart,
        myStart,
        myEnd,
    ) = goOn

    api = app.api
    F = api.F
    L = api.L
    T = api.T
    otypeRank = api.otypeRank
    isHtml = options.get('fmt', None) in app.textFormats

    bigType = (
        not d.full
        and
        d.condenseType is not None and otypeRank[nType] > otypeRank[d.condenseType]
    )

    (hlClass, hlStyle) = hlAtt

    heading = ''
    featurePart = ''
    children = ()

    if bigType:
      children = ()
    elif nType == 'book':
      children = L.d(n, otype='chapter')
    elif nType == 'chapter':
      children = L.d(n, otype='sentence')
    elif nType == 'sentence':
      children = L.d(n, otype='word')
    elif nType == 'line':
      children = L.d(n, otype='word')
    else:
      children = L.d(n, otype='word')

    isText = False

    if nType == 'book':
      heading = htmlEsc(F.title.v(n))
      heading += ' '
      heading += getFeatures(
          app,
          n,
          ('author',),
          plain=True,
          **options,
      )
    elif nType == 'chapter':
      heading = htmlEsc(F.number.v(n))
      featurePart = getFeatures(
          app,
          n,
          (),
          **options,
      )
    elif nType == 'sentence':
      heading = htmlEsc(F.number.v(n))
      featurePart = getFeatures(
          app,
          n,
          (),
          **options,
      )
    elif nType == 'line':
      heading = F.number.v(n)
      featurePart = getFeatures(
          app,
          n,
          ('terminator',),
          **options,
      )
    elif nType == slotType:
      isText = True
      text = T.text(n, fmt=d.fmt)
      heading = text if isHtml else htmlEsc(text)
      featurePart = getFeatures(
          app,
          n,
          ('gap',),
          withName=True,
          **options,
      )

    tClass = display.formatClass[d.fmt].lower() if isText else app.defaultCls
    heading = f'<span class="{tClass}">{heading}</span>'

    if outer:
      typePart = app.webLink(n, text=f'{nType} {heading}', _asString=True)
    else:
      typePart = heading

    label = f'''
    <div class="lbl {className}">
        {typePart}
        {nodePart}
    </div>
''' if typePart or nodePart else ''

    html.append(
        f'''
<div class="contnr {className} {hlClass}" {hlStyle}>
    {label}
    <div class="meta">
        {featurePart}
    </div>
'''
    )
    if children:
      html.append(f'''
    <div class="children {className}">
''')

    for ch in children:
      app._pretty(
          ch,
          False,
          html,
          firstSlot,
          lastSlot,
          **options,
      )
    if children:
      html.append('''
    </div>
''')
    html.append('''
</div>
''')
