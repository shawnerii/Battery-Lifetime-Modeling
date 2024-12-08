import sort_data
import predict_capacity


def main():
    PL03c, PL03d = sort_data.charge_discharge('data/converted_PL03.mat')
    full_curvesc, full_curvesd = sort_data.charge_discharge('data/converted_PL04.mat')

    # Make a shorter partial curve dictionary to uses as train set (because if not the code takes too long)
    PL03d_short = {}
    for idx in range(1, len(PL03d.keys()), 50):
        if idx in PL03d.keys():
            if idx not in PL03d_short.keys():
                PL03d_short[idx] = PL03d[idx]
    full_curvesd_short = {}
    for idx in range(1, len(full_curvesd.keys()), 50):
        if idx in full_curvesd.keys():
            if idx not in full_curvesd_short.keys():
                full_curvesd_short[idx] = full_curvesd[idx]

    Percent, Time, Slope, Intercept, Life = predict_capacity.get_lifetime(PL03d_short, full_curvesd_short, 1.5)
    predict_capacity.life_plot(Time[0], Slope[0], Intercept[0], Percent[0], Life[0])


if __name__ == "__main__":
    main()
