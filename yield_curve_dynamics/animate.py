from matplotlib import animation
import matplotlib.pyplot as plt


def create_animation(curves, timegrid, n_frames=None, frame_millis=100):
    if not n_frames or n_frames >= len(curves):
        step = 1
        n_frames = len(curves)
    else:
        step = int(len(curves) / n_frames)
    assert step > 0

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 30)
    ax.set_ylim(-1, 5)
    ttl = ax.text(28, 4.8, "")

    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        dt, curve = curves[i*step]
        y = curve(timegrid)
        line.set_data(timegrid, y)
        ttl.set_text('{}-{:02d}'.format(dt.year, dt.month))
        return (line, ttl)

    return animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=frame_millis,
                                   blit=True)
