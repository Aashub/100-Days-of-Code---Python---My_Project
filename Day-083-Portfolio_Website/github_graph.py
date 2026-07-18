import os
import requests
import json
from datetime import  datetime


# Github GraphQl API query to fetch all the required data.
query = """{

  viewer {

    repositories{
        totalCount
    }

    contributionsCollection {
      contributionCalendar {
        totalContributions
      }
    }


    contributionsCollection {
      contributionCalendar {
        weeks{
            contributionDays{
                color, contributionCount, contributionLevel, date
            }
        }
      }
    }

    repositories{
        nodes{
           stargazerCount,forkCount
        }
    }

   }

}"""

GITHUB_GRAPH_QL_ENDPOINT = os.environ["GITHUB_GRAPH_QL_URL"]

headers = {
    "Authorization": os.environ["ACCESS_TOKEN"],
    "Content-Type": "application/json"

}


class GithubData:
    """this class is responsible for fetching required github data for contribution graph and store those value in so it can be used."""

    def __init__(self):

        self.github_url = GITHUB_GRAPH_QL_ENDPOINT
        self.response = requests.post(self.github_url, json={"query": query}, headers=headers)


    def checking_response(self):
        """this method checks that GitHub data is being retrieved successfully or not."""

        if self.response.status_code == 200:
            print("the data is retrieved successfully")

            return 0

        else:
            print(f"Query failed with status code {self.response.status_code}: {self.response.text}")
            return 1

    def fetching_required_data(self):
        """"this method fetch data like repository count, total stars, total forks, total contributions"""


        github_data = self.response.json()


        # # repository count
        repository_count = github_data["data"]["viewer"]["repositories"]["totalCount"]

        # to get total stars
        total_stars = sum([star["stargazerCount"] for star in github_data["data"]["viewer"]["repositories"]["nodes"]])

        # to total forks
        total_forks = sum([star["forkCount"] for star in github_data["data"]["viewer"]["repositories"]["nodes"]])

        # total Contribution
        total_contribution = github_data["data"]["viewer"]["contributionsCollection"]["contributionCalendar"][
            "totalContributions"]


        return repository_count, total_stars, total_forks, total_contribution

    def fetch_month_labels(self):
        """this method fetch data like graph contribution data and months label list"""


        github_data = self.response.json()

        month_label_list = []

        # graph contribution data
        graph_contribution_data = github_data["data"]["viewer"]["contributionsCollection"]["contributionCalendar"][
            "weeks"]

        # this for loop look for the month label and store that month label into a list.
        for week in graph_contribution_data:
            first_day = week["contributionDays"][0]["date"]

            formated_date = datetime.strptime(first_day,
                                              "%Y-%m-%d")  # converting each week first date into datetime format
            month = formated_date.strftime("%b")  # changing the formated date into this format "Jul Aug"

            if month not in month_label_list:
                month_label_list.append(month)

            else:
                month_label_list.append("")


        return graph_contribution_data, month_label_list

