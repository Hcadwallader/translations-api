# translations-api

## Getting started guide

Note FE url to be updated to
`const TRANSLATION_SERVICE_URL = 'http://127.0.0.1:8080/translate';`

This was developed using python version 3.12.4

I used a venv to manage packages, see link for details
https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511

To run api application
`python app.py`

To run tests
`pytest`

To get docker container running with LibreTranslate
`docker compose up`

## Questions

- If you used any particular libraries why did you choose them?

    - Flask - I choose to use this as it's simple to set up, easy to understand and add to.
    - Pytest - Industry standard testing framework
    - Requests - Industry standard http client library
    - pyspellchecker - Top rated native python spell checker package

- Which translation API did you use and why?

I used LibreTranslate as it was the recommended option and I didn't want use a paid API, so this fufilled all criteria.

- Did you make any assumptions, or take any shortcuts?

    - Assumptions
        - Request data valid input
        - Only alpha characters are valid

    - Shortcuts
        - Accepted default algorithm for pyspellchecker which for example wrongly correctly 'Gracias' to 'Gracious'

- Did you have any challenges and if so, how did you overcome them?

    - When running LibreTranslate initially I was running into a segmentation fault issue, that I thought was linked to python version running on my machine. Therefore, I decided to set up LibreTranslate to run in a docker container which resolved the issue. See docker-compose and instructions above for how to run.
    - Once running in docker I was getting response code 400: bad request, which I thought might be linked to invalid characters in the words so implemented clean_word to strip these out. However, the actual issue was the docker image not having all the models for all language translation options. This was corrected by running update-models which then brought down all missing models.


- Did you add any extra features?

No

- If you had more time, what else would you implement?

    - Add package or api to detect non-english words
    - Consider a more accurate spellcheck, some words such as 'helo' corrected to 'help' when could be 'hello' mispelt
    - Add more graceful error handling
        - i.e. if single translate fails the whole batch of translated worlds lost so implement for example retries, splitting into small batches something like that
        - invalid format of data sent to translate
    - input validation
        - Is in expected format
    - Add tests for translate_api
    - Add tests for api endpoint
    - Add integration test(s)
    - Investigate rate limiting to prevent overwhelming LibreTranslate
