from local import OSdist, Ul


def rtl(text):
    if (Ul == 'he') or (Ul == 'ar') or (Ul == 'arc') or (Ul == 'dv') or (Ul == 'fa') or (Ul == 'ha') or (Ul == 'khw') or (Ul == 'ku') or (Ul == 'ps') or (Ul == 'ur') or (Ul == 'yi'):
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
    else:
        return text
