# wordlists
Own (or modified) wordlists
fuzzer/ 
- 1mln_chars_pleaseignore.txt - for buffer overflow

DNS/
- subdomains_wordlist - based on SecLists subdomains-top1mil-110000.txt but without duplicates and upper domains (I can be mistaken here and we should include uppercase domains)

Password/
- Russian/ - wordlist based on yandex.ru, gmail.com, mail.ru leak ( *** in progress *** - needs to be sorted by frequency and remove duplicates )

Usernames/
- russian_surnames/ - parsed http://www.edudic.ru/fam/
- http_parser_title_file.py - http parser (with progress bar), usage: http_parser_title_file.py -o output_file.txt
