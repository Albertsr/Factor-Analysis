def get_scale(df):
    def scale_func(series):
        avg = np.mean(series)
        std = np.std(series, ddof=0)
        return (series-avg) / (np.sqrt(len(series)) * std)
    
    res = np.apply_along_axis(scale_func, arr=df, axis=0)
    return res.round(2)