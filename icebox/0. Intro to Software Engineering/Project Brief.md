# Your first package: Project Brief

In the last project, you created a scraper that was able to extract data from one or multiple webpages, and then store that data for future use. The project was great, and your scraper works as expected. However, it is your project, and as such, it is very unlikely that other developers can navigate through it easily. If other developers find it hard to use it, let alone publishing it for the general public!

Therefore, this second project is more like an extension of the first one, where you are going to improve your current code, implementing all the best practices we are going to learn during this unit. 

## What do we expect?

By the end of the project, the rest of the classmates will download your package. If you are unable to upload it, you will have another chance by making it public in GitHub.

Ideally, your classmates will type `pip install <name of your package>` and they will be able to use the package anywhere in their computer. 

If you are unable to do so, we will substract points for not publishing it, but again, you can still pass this unit if your package is public in GitHub with the proper structure as explained later. 

Apart from that, your package will include a model to write data to an AWS RDS. That data should be the data you include, but if your data is not tabular, you can simply create a code that works for other tabular data.

> ## By the end of the project, this is how your project should look like

```
root/
│
├── project
│   ├── scraper
│   │    ├── __init__.py
│   │    ├── scraper_module_1.py
│   │    └── scraper_module_2.py
│   │
│   │
│   └── rds_uploader
│        ├── __init__.py
│        ├── rds_module_1.py
│        └── rds_module_2.py
│
├── test
│   ├── test_project.py
│   ├── test_module_1.py
│   └── test_module_2.py
│   
├── README.md
├── setup.py
├── setup.cfg
├── LICENSE
└── .gitignore
```

__Of course, change the name of your files accordingly__

Your packages DON'T NEED to have two modules each, but if a module doesn't present a logical level of abstraction and encapsulation, that will substract points to your project.

## Deliverables

In this case, you only need to give a presentation. BUT the presentation will be you selling your package. We want to see you are comfortable with your work, and that you are able to explain it with no issue at all. No one is going to buy your product if not even you trust it. 

The presentation will consist on 

- A brief summary of your project (we already saw that during the first project, so you don't have to give too much detail)
- The name of your package, and how the rest of your classmates can download it
- A walkthrough the modules of your package, a basic `How-To-Use` tutorial
- Pretend the rest of your classmates are regular users, with very basic Python knowledge. You have to explain how use the rds_uploader.

You will have _up to_ 15 minutes to present your project, so make them count!

## When?

The presentations are due on 30th August (3 weeks from now). You will have one week to dedicate solely to the project, but, try to start ASAP. 

## Final Note

I know you are doing a great job, don't feel overwhelmed about the amount of you have to put into the project. I will guide you through ALL the steps to publish the package. 

Don't take these projects as homework or as a way to measure your performance for us. Everything we are doing is going to help you to develop your skillset for your future career. Of course, we, the AiCore team, need to set some standards, so that's the reason of being sometimes strict. 

Take these projects as an opportunity to showcase your abilities to recruiters. It is easy to say that you know SQL and get a certification that everyone has. But what not everyone has is a great project that shows it. 

After all, it is your life, you take the reins of it, and it's up to you what you want to do with it, we are here to boost your career, so make the most out of our assistance!