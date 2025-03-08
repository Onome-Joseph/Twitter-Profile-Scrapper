# **X Automation and Scrapping using Selenium & Bs4**  

This project is a **Python-based web scraper** that extracts X profile details using **Selenium and BeautifulSoup4**. The script automates **X login**, navigates to user profiles, and retrieves:  

- **Bio**  
- **Following Count**  
- **Followers Count**  
- **Location**  
- **Website (if available)**

## **The extracted data is stored in a **CSV file** for further analysis.**  

---
- **Automated Login:** Logs into X using provided credentials.  
- **Scrapes Multiple Profiles:** Reads links from a CSV file and extracts profile details.  
- **Handles Restricted Profiles:** Ensures authentication before scraping.  
- **Error Handling:** Skips missing elements to avoid script failure.  
---

## **Installation & Setup**
### **1 Clone the Repository**  
```bash
git clone https://github.com/Onome-Joseph/X-Profile-Scrapping.git
```

### **2 Install Dependencies**    
```bash
pip install -r requirements.txt
```

### **3 Configure Login Credentials**  
Open `X_bot.py` and **replace** the placeholders with your **X(twitter) credentials** in the config.json file.

