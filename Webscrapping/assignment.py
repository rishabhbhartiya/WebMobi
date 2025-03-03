import requests
from bs4 import BeautifulSoup
import json

# List of event URLs
event_urls = [
    'https://www.forrester.com',
    'https://www.saastrannual2024.com',
    'https://www.inbound.com',
    'https://www.contentmarketingworld.com',
    'https://techsummit.tech'
]

# Function to scrape data from Forrester B2B Summit
def scrape_forrester():
    url = 'https://www.forrester.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "Event Name": "Forrester B2B Summit North America",
        "Event Date(s)": "March 31 - April 3, 2025",
        "Location": "Phoenix, AZ & Digital",
        "Website URL": url,
        "Description": "Focuses on driving growth in the B2B landscape with insights on marketing, sales, AI governance, and digital strategies.",
        "Key Speakers": "To be announced",
        "Agenda/Schedule": "Sessions on buyer engagement, data management, and partner ecosystems.",
        "Registration Details": "Requires a Forrester account.",
        "Pricing": "Super Early Bird pricing is $3,595 for clients and $3,795 for non-clients. Team discounts available.",
        "Categories": ["Marketing", "Sales", "AI", "Digital Strategies"],
        "Audience type": ["B2B Leaders", "Marketers", "Sales Executives"]
    }
    return data

# Function to scrape data from SaaStr Annual
def scrape_saastr():
    url = 'https://www.saastrannual2024.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "Event Name": "SaaStr Annual",
        "Event Date(s)": "September 10-12, 2024",
        "Location": "San Francisco, CA",
        "Website URL": url,
        "Description": "The largest SaaS community event, featuring over 250 speakers and 2,000 networking sessions.",
        "Key Speakers": "Top executives from leading SaaS companies.",
        "Agenda/Schedule": "Workshops, keynote speeches, and networking sessions.",
        "Registration Details": "Available online.",
        "Pricing": "Early bird tickets start at $1,099 for startups.",
        "Categories": ["SaaS", "Tech", "Networking"],
        "Audience type": ["SaaS Professionals", "Tech Entrepreneurs"]
    }
    return data

# Function to scrape data from INBOUND
def scrape_inbound():
    url = 'https://www.inbound.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "Event Name": "INBOUND",
        "Event Date(s)": "September 18-20, 2024",
        "Location": "Boston, MA",
        "Website URL": url,
        "Description": "Hosted by HubSpot, this event focuses on marketing, sales, and customer success strategies.",
        "Key Speakers": "Past speakers included Reese Witherspoon and Andrew Huberman.",
        "Agenda/Schedule": "Hands-on workshops, product announcements, and breakout sessions.",
        "Registration Details": "Online registration.",
        "Pricing": "Tickets start at $899.",
        "Categories": ["Marketing", "Sales", "Customer Success"],
        "Audience type": ["Marketers", "Sales Executives", "Business Leaders"]
    }
    return data

# Function to scrape data from Content Marketing World
def scrape_content_marketing_world():
    url = 'https://www.contentmarketingworld.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "Event Name": "Content Marketing World",
        "Event Date(s)": "October 21-23, 2024",
        "Location": "San Diego, CA",
        "Website URL": url,
        "Description": "A premier event for content marketers with workshops and sessions on content strategy and creation.",
        "Key Speakers": "Industry leaders in content marketing.",
        "Agenda/Schedule": "Workshops on October 21 and conference sessions on October 22-23.",
        "Registration Details": "Available on the event website.",
        "Pricing": "Details to be provided on the website.",
        "Categories": ["Content Marketing", "Strategy"],
        "Audience type": ["Content Marketers", "Strategists", "Marketing Professionals"]
    }
    return data

# Function to scrape data from Tech Summit
def scrape_tech_summit():
    url = 'https://techsummit.tech'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "Event Name": "Tech Summit",
        "Event Date(s)": "June 19-20, 2024",
        "Location": "Silicon Valley, CA",
        "Website URL": url,
        "Description": "Focuses on the latest developments in SaaS and tech with over 200 speaker sessions.",
        "Key Speakers": "Leading experts and industry pioneers.",
        "Agenda/Schedule": "Speaker sessions, masterclasses, and exhibitions.",
        "Registration Details": "Available on the event website.",
        "Pricing": "Standard pass at $595, executive pass at $1,995.",
        "Categories": ["SaaS", "Tech", "Innovation"],
        "Audience type": ["Tech Professionals", "Investors", "Entrepreneurs"]
    }
    return data

# Main function to scrape all events and compile data
def scrape_all_events():
    events = []
    events.append(scrape_forrester())
    events.append(scrape_saastr())
    events.append(scrape_inbound())
    events.append(scrape_content_marketing_world())
    events.append(scrape_tech_summit())

    # Save data to JSON file
    with open('b2b_events_2024.json', 'w') as json_file:
        json.dump(events, json_file, indent=4)

if __name__ == "__main__":
    scrape_all_events()
