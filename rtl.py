from local import OSdist


def rtl(text):
    if OSdist == 'Lin':
        try:
            textdec = unicode(text, 'utf-8')
            textrev = textdec[::-1]
            return textrev
        except:
            textrev = text[::-1]
            return textrev
    if OSdist == 'Win':
        return text
