#!/usr/bin/env python
"""

In order to use mathtext, you must build matplotlib.ft2font.  This is
built by default in the windows installer.

For other platforms, edit setup.py and set

BUILD_FT2FONT = True

"""
from matplotlib.matlab import *
subplot(111, axisbg='y')
plot([1,2,3])
x = arange(0.0, 3.0, 0.1)
#plot(x, sin(2*pi*x))
grid(True)
xlabel(r'$\Delta_i^j$', fontsize=20)
ylabel(r'$\Delta_{i+1}^j$', fontsize=20,  # no rotation yet for mathtext
       verticalalignment='center',
       horizontalalignment='right',
       rotation='horizontal')
tex = r'$\cal{R}\prod_{i=\alpha_{i+1}}^\infty a_i\rm{sin}(2 \pi f x_i)$'
#tex = r'$\cal{R}\prod^\infty a_i\rm{sin}(2 \pi f x_i)$'

#tex = r'$\alpha\beta\gamma$'
text(1, 2.6, tex, fontsize=20)
title(r'$\Delta_i^j \hspace{0.4} \rm{versus} \hspace{0.4} \Delta_{i+1}^j$', fontsize=20)
#savefig('mathtext_demo_small', dpi=100)
savefig('mathtext_demo_large', dpi=300)

show()
