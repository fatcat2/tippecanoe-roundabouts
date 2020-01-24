from openpyxl import load_workbook
import pandas as pd
import matplotlib.pyplot as plt

def get_plot(wb):
    counts = []
    for year in ["2017", "2018", "2019"]:
        year_data = pd.DataFrame(wb[year].values)

        filtered_data = year_data[year_data[2]=="STATESTTAPAWINGODR"]
        filtered_data_2 = year_data[year_data[2]=="STATESTTAPAWINGORD"]
        combined_filtered_data = pd.concat([filtered_data, filtered_data_2])

        print(combined_filtered_data[5].value_counts())

        counts.append([year, len(combined_filtered_data.index)])
    print(counts)
        # print(len(combined_filtered_data[combined_filtered_data[5]=="SAME DIRECTION SIDESWIPE"].index))

    df = pd.DataFrame(counts, columns = ['year', 'count'])
    df.plot(kind='bar',x='year',y='count')
    plt.show()


def get_accident_plot(wb):
    year_data = pd.DataFrame(wb["2019"].values)
    year_data = year_data.iloc[1:]
    year_data.columns = ["date", "time", "location_id", "injured", "dead", "collision"]
    
    filtered_data = year_data[year_data["location_id"]=="STATESTTAPAWINGODR"]
    filtered_data_2 = year_data[year_data["location_id"]=="STATESTTAPAWINGORD"]
    combined_filtered_data = pd.concat([filtered_data, filtered_data_2])

    combined_filtered_data["collision"].value_counts().plot(kind="bar")
    plt.show()

def get_top_wl_intersections():
    data = [
        ["State St/Tapawingo Dr", 44],
        ["Sagamore Parkway/North Salisbury", 40],
        ["River Rd./Tapawingo Dr.", 37],
        ["Cumberland Ave./Sagamore Pkwy", 22],
        ["Northwestern Ave./Yeager Drive", 19]
    ]

    df = pd.DataFrame(data, columns = ["Intersection", "Accident count"])
    df.plot(kind="bar", x="Intersection", y="Accident count")
    plt.show()

def get_top_ten(wb):
    top_ten = {year: pd.DataFrame(wb[year].values)[2].value_counts()[0:50] for year in ["2017", "2018", "2019"]}
    return top_ten


def main():
    wb = load_workbook("2017-19 crash data.xlsx")
    get_top_wl_intersections()


if __name__=="__main__":
    main()
