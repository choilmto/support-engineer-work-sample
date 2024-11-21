______
While testing on my local development machine, I used the public machine api (https://api.machines.dev), but for testing in deployment, I replaced the public machine api with the internal one (http://_api.internal:4280). As fly.io documentation specifies, I set the header of my network request to the api so it contained a token generated using the fly cli. Once the deployment worked, I replaced the real token with some dummy text.

I configured my request and retrieved the information for the machine that the application is deployed on. I used the 'apps' uri, which supplied lots of information about my specific application, called 'python-django'. Python, like other languages, makes it easy to turn text into objects (dicts), so I did with the json library.

TemplateView has a few methods, one of which is get_context_data. I supplied the homepage template with the object made from the json string. The template already anticipated the object's fields as they are. I did not have to create a new object to fit the shape of the machines object in the template. Also, I did not pare the object down to only the fields that the template called for (id, name, config.image, created_at, region, private_ip, state)

I included the changes to settings.py as suggested to get my deployment running. Also, I included the changes to fly.toml after deploying.
______
