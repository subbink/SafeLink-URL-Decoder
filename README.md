### SafeLink URL Decoder

SafeLink URL Decoder is a Python script designed to decode SafeLink URLs and reveal their final destination. It handles nested URLs and removes fragments to provide a clean final URL.

Example of a SafeLink URL:
```
https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fscanner.topsec.com%2F%3Fd%3D3744%26r%3Dauto%26u%3Dhttps%253A%252F%252Fmaknastudio.com%252Fpkyos%26t%3Da4fe2e96fe6815a71cc8a7f1ae1196e6fbcf1f08&data=05%7C02%7CRyan.Esligar%40englobecorp.com%7C56329498418f4cffe2f808dc9a8d586a%7Cb35ebd72daad43b9b2465087acbf3b69%7C0%7C0%7C638555179070943625%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C20000%7C%7C%7C&sdata=oBKbVLsB3X7kDEi%2FoDASrG%2F42MvaSIQclYuKJ5j15p8%3D&reserved=0
```

#### How It Works
1. **Enter SafeLink URL**: Users enter the SafeLink URL when prompted by the script.
2. **Decode URL**: The script decodes the 'url' parameter from the SafeLink URL.
3. **Check for Additional URL**: If the decoded URL contains another URL inside it, that URL is also decoded.
4. **Remove Fragment**: The script removes any fragment from the final URL.
5. **Print Final URL**: The clean final URL is printed.

#### Usage
1. Run the script.
2. Enter the SafeLink URL when prompted.
3. The script will print the final decoded URL.

#### Disclaimer
Copyright © 2024 Mahdi Aggoun. All rights reserved.

This software is provided "as is" without any warranties. The user assumes all responsibility for any damages or losses that may occur as a result of using this tool. Unauthorized reproduction or distribution of this software may result in legal consequences.
