import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    rows, cols = df.shape

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # 1
    race_count = df['race'].value_counts()

    # What is the average age of men?
    filter_sex_male = (df['sex'] == 'Male')
    # 2
    average_age_men = round(df.loc[filter_sex_male, 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    filter_education_bachelors = (df['education'] == 'Bachelors')
    total_education_bachelors = filter_education_bachelors.sum()
    # 3
    percentage_bachelors = round(total_education_bachelors / rows * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filter_education_masters = (df['education'] == 'Masters')
    filter_education_doctorate = (df['education'] == 'Doctorate')

    # percentage with salary >50K
    filter_salary_rich = (df['salary'] == '>50K')

    filter_higher_education = filter_education_bachelors | filter_education_masters | filter_education_doctorate
    filter_higher_education_rich = filter_salary_rich & filter_higher_education
    total_higher_education = filter_higher_education.sum()
    total_higher_education_rich = filter_higher_education_rich.sum()
    # 4
    higher_education_rich = round(total_higher_education_rich / total_higher_education * 100, 1)

    filter_lower_education = ~filter_higher_education
    filter_lower_education_rich = filter_salary_rich & filter_lower_education
    total_lower_education = filter_lower_education.sum()
    total_lower_education_rich = filter_lower_education_rich.sum()
    # 5
    lower_education_rich = round(total_lower_education_rich / total_lower_education * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # 6
    min_work_hours = round(df['hours-per-week'].min(), 1)
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    filter_min_hours = (df['hours-per-week'] == min_work_hours)
    filter_min_hours_rich = filter_salary_rich & filter_min_hours
    total_min_hours = filter_min_hours.sum()
    total_min_hours_rich = filter_min_hours_rich.sum()
    # 7
    rich_percentage = round(total_min_hours_rich / total_min_hours * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    df_salary_rich = df[(filter_salary_rich) & df['native-country']]
    df_salary_rich_country = (df_salary_rich['native-country'].value_counts()) / (df['native-country'].value_counts()) * 100
    # 8
    highest_earning_country = df_salary_rich_country.idxmax()
    # 9
    highest_earning_country_percentage = round(df_salary_rich_country.loc[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    # 10
    top_IN_occupation = df['occupation'].value_counts().idxmax()   

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
