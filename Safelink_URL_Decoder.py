import urllib.parse

# Prompt the user to enter the SafeLink URL
safelink = input("Enter the SafeLink URL: ")

try:
    # Analyse the SafeLink URL to extract its components
    parsed_url = urllib.parse.urlparse(safelink)
    
    # Extract the query parameters from the SafeLink URL
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Check if the 'url' parameter exists in the query parameters
    if 'url' in query_params:
        # Decode the 'url' parameter value
        decoded_url = urllib.parse.unquote(query_params['url'][0])

        # Check the decoded URL for nested query parameters.
        nested_query_params = urllib.parse.parse_qs(urllib.parse.urlparse(decoded_url).query)
        
        # If a nested 'url' parameter exists, decode it
        if 'u' in nested_query_params:
            nested_url = nested_query_params['u'][0]
            final_url = urllib.parse.unquote(nested_url)
        else:
            # If no nested 'u' parameter, use the decoded URL as the final URL
            final_url = decoded_url

        # Parse the final URL to handle and remove any fragments
        final_parsed_url = urllib.parse.urlparse(final_url)
        final_url_without_fragment = final_parsed_url._replace(fragment='').geturl()

        # Print the final URL without the fragment
        print(f"Final URL: {final_url_without_fragment}")
    else:
        # Print a message if the 'url' parameter is missing
        print("The provided SafeLink URL does not contain a 'url' parameter.")
except Exception as e:
    # Print any error that occurs during the process
    print(f"An error occurred: {e}")
