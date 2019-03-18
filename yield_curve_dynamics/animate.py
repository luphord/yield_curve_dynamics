from matplotlib import animation, rc
import matplotlib.pyplot as plt

def create_animation(curves, timegrid, n_frames):

    step = int(len(curves) / n_frames)
    assert step > 0

    fig, ax = plt.subplots(figsize=(12,8))
    ax.set_xlim(0, 30)
    ax.set_ylim(-1, 5)
    ttl = ax.text(28,4.8,"")

    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        dt, curve = curves[i*step]
        y = curve(timegrid)
        line.set_data(timegrid, y)
        ttl.set_text('{}-{:02d}'.format(dt.year, dt.month))
        return (line,ttl)

    return animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=100,
                                   blit=True)