# IntraBotnyx: Your Organization's Intelligent Offline Assistant

* "IntraBotnyx" is a revolutionary project enabling businesses and organizations to harness Large Language Models (LLMs) within their secure intranet environments, eliminating dependence on the internet. By integrating LLMs from diverse sources into Local Area Networks (LANs), it ensures offline access and upholds data security. Notably, it optimizes LLM performance on standard hardware, facilitating widespread AI integration for various tasks and workflow automation. Additionally, it deploys intelligent chatbots tailored to organization-specific data, fostering inter-departmental collaboration and enhancing employee support across functions from Human Resources to Business Intelligence.

Our proof of concept approach will consist of a Django website running on localhost , and we plan on using vicuna-13B via GGML format to run on CPUs for general chat functionalities and special fine tuned version of google’s T5 language Model for news article summarisation all running locally on consumer grade hardware without internet connection.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to create a virtual environment and run this command in your terminal.

```
pip install -r requirements.txt
```


### Installing

A step by step series of code that tell you how to get a development env running


By installing Django Package:-
```
pip install django
```
Check version of django:-
```
django-admin --version
```
Run server:-
```
 python manage.py runserver
```


End with an example of getting some data out of the system or using it for a little demo



## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Versioning

<!-- We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## Authors

* **Dhritiman Senpramanik** 
* **Sahil Patel**
* **Mansi Raval**
* **Aksh Desai**
* **Mitren Kadiwala**
* **Meshv Patel**

## References

https://pub.towardsai.net/fine-tuning-a-llama-2-7b-model-for-python-code-generation-865453afdf73

https://huggingface.co/t5-11b

https://huggingface.co/mrm8488/t5-base-finetuned-summarize-news

https://github.com/ggml-org/p1/discussions/1


<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## License

This project is licensed under the MIT License 

<!-- - see the [LICENSE.md](LICENSE.md) file for details -->

## Acknowledgments

* Hat tip to anyone whose code was used
* This effort was made to create a one-stop solution