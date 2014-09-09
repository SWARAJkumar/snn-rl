from architecture import *

dictionary = dictionary()
spiketimes = dictionary.spikeTimes(dictionaryLongitude, spikeInterval, spikesPerChar, epochs)
LIK = SpikeGeneratorGroup(15, spiketimes)
M = SpikeMonitor(LIK)

run(spikesPerChar * dictionaryLongitude * spikeInterval , report='text')
raster_plot(M, title='First layer', newfigure=False)
show()
