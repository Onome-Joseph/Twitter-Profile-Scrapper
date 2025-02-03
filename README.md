# **Twitter Profile Scraper using Selenium**  

This project is a **Python-based web scraper** that extracts Twitter profile details using **Selenium**. The script automates **Twitter login**, navigates to user profiles, and retrieves:  

- **Bio**  
- **Following Count**  
- **Followers Count**  
- **Location**  
- **Website (if available)**  

The extracted data is stored in a **CSV file** for further analysis.  
---
## **Features**  
 **Automated Login:** Logs into Twitter using provided credentials.  
 **Scrapes Multiple Profiles:** Reads links from a CSV file and extracts profile details.  
 **Handles Restricted Profiles:** Ensures authentication before scraping.  
 **Error Handling:** Skips missing elements to avoid script failure.  
---

## ** Installation & Setup**  
### **1 Clone the Repository**  
```bash
git clone https://github.com/Onome-Joseph/Twitter-Profile-Scraper.git
```

### **2 Install Dependencies**    
```bash
pip install -r requirements.txt
```

### **3 Configure Login Credentials**  
Open `twitter_scraper.py` and **replace** the placeholders with your **Twitter username and password**:  
```python
TWITTER_USERNAME = "your_username"
TWITTER_PASSWORD = "your_password"
```
