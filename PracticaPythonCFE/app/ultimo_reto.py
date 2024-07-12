import read_csv
import utils
import charts


def run():
    data = read_csv.read_csv('/home/alejandroantezana/PycharmProjects/pythonProject/PracticaPythonCFE/app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentage = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentage)


if __name__ == '__main__':
    run()
