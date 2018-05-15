import requests

username = "ARCHIVE-IT_USERNAME"
password = "ARCHIVE-IT_PASSWORD"
api_base_url = "https://partner.archive-it.org/api/"
api_login_url = "https://partner.archive-it.org/api-auth/login/"
client = requests.session()
client.get(api_login_url)
csrftoken = client.cookies["csrftoken"]
login_data = dict(username=username, password=password, csrfmiddlewaretoken=csrftoken, next="/")
headers = dict(Referer=api_login_url)
login = client.post(api_login_url, data=login_data, headers=headers, cookies=client.cookies)

# GET AN INDIVIDUAL SEED
seed_id = "ARCHIVE-IT_SEED_ID"  # e.g., 896198
seed_url = api_base_url + "seed/{}".format(seed_id)
seed_json = client.get(seed_url, headers=headers, cookies=client.cookies).json()

# GET ALL SEEDS ASSOCIATED WITH AN ARCHIVE-IT ACCOUNT
archive_it_organization_id = "ARCHIVE-IT_ORGANIZATION_ID"  # e.g., 934
seeds_url = api_base_url + "seed?account={}".format(archive_it_organization_id)
seeds_json = client.get(seeds_url, headers=headers, cookies=client.cookies).json()

# EXTRACT ONLY PUBLICLY VISIBLE SEEDS
public_seeds = [seed for seed in seeds_json if seed["publicly_visible"]]

# EXTRACT ONLY ACTIVELY CAPTURED SEEDS
active_seeds = [seed for seed in seeds_json if seed["active"]]

# EXTRACT ALL UNIQUE SUBJECTS
# USEFUL FOR DATA CLEANUP AND RECONCILIATION
subjects = []
for seed in seeds_json:
    seed_metadata = seed["metadata"]
    for subject in seed_metadata.get("Subject", []):
        subject_value = subject["value"]
        if subject_value not in subjects:
            subjects.append(subject_value)
