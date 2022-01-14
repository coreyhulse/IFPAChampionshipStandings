I am the IFPA NACS State and Provincial Championship Bot.

Link to Add Bot to Discord: https://discord.com/api/oauth2/authorize?client_id=927940692297281566&permissions=534723951680&scope=bot


Type $ifpachamps_nacs or $ifpachamps_wnacs followed by the following two inputs:

* Two-Letter State or Province Code
* Year

I will attempt to return the top 32 players for the year requested.
Example: $ipfachamps_nacs PA 2022
Example: $ipfachamps_wnacs PA 2022

The Womens standings relies on a lookup table stored in my GitHub repository (wnacs.csv).  If you see a state missing please log an issue on GitHub.

Commands to Try:
$ifpahelp - Help Response
$ipfachamps_nacs PA 2021 - Location That Works
$ipfachamps_nacs PJ 2021 - Location That Does Not Work
$ipfachamps_wnacs PA 2022 - Location That Works
$ipfachamps_wnacs YT 2022 - Location That Exists, But No URL Mapped
$ipfachamps_wnacs PJ 2022 - Location That Does Not Work

Version 2.0 (2022-01-14):
* Supports the WNACS

Version 1.0 (2022-01-06):
* Supports the NACS

If you'd like to see or request new features please drop an "Issue" on GitHub!