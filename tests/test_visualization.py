import os
import tempfile
from src.visualization import plot_histogram, plot_kde, plot_lag


def test_plot_histogram_saves_file():
    classical = list(range(256))
    quantum = list(range(256))
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "hist.png")
        plot_histogram(classical, quantum, save_path=path)
        assert os.path.exists(path)


def test_plot_kde_saves_file():
    classical = list(range(256))
    quantum = list(range(256))
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "kde.png")
        plot_kde(classical, quantum, save_path=path)
        assert os.path.exists(path)


def test_plot_lag_saves_file():
    data = list(range(256))
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "lag.png")
        plot_lag(data, "Test", save_path=path)
        assert os.path.exists(path)
