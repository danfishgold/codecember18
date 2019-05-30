from __future__ import division
import os


filename_description = ''


def image_saving_key_event_handler(base_filename, extension='png'):
    global filename_description
    if isinstance(key, unicode):
        if key == '\n':
            files = os.listdir('.')
            matches = [
                match(f, r'{}_(\d+).*\.{}'.format(base_filename, extension)) for f in files]
            indexes = [int(m[1]) for m in matches if m is not None]
            if indexes:
                index = max(indexes) + 1
            else:
                index = 1

            if filename_description:
                modifier = '_{}'.format(filename_description.replace(' ', '_'))
            else:
                modifier = ''
            filename = '{}_{:02d}{}.{}'.format(
                base_filename, index, modifier, extension)

            save(filename)
            print 'saved', filename
            filename_description = ''
        else:
            if key == BACKSPACE:
                filename_description = filename_description[:-1]
            else:
                filename_description = filename_description + key


def hex_to_rgb(string, alpha=None):
    h = string.lstrip('#')
    r, g, b = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    if alpha is not None:
        return r, g, b, alpha
    else:
        return r, g, b


def hide_outside_circle():
    side = min(width, height)
    pushStyle()
    pushMatrix()
    strokeWeight(side)
    stroke(color(255))
    noFill()
    ellipse(width/2, height/2, 1.8*side, 1.8*side)
    popMatrix()
    popStyle()


def distribute(v_min, v_max, count=None, shift=None):
    if count and shift:
        raise ValueError("Set either the count or the shift. Not both")
    if count:
        shift = (v_max - v_min) / (count-1)
        return [v_min + idx*shift for idx in range(count)]
    else:
        og_width = v_max - v_min
        count = int(floor(og_width / shift + 1e-7))
        width = count*shift
        diff = (og_width - width)/2
        return distribute(v_min+diff, v_max-diff, count=count+1)


def cubic_ease(f):
    return 3*f*f - 2*f*f*f
