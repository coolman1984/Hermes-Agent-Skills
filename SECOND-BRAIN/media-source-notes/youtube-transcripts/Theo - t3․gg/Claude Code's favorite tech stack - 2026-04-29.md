# Transcript — v1MptV67kSI

**Source:** https://youtube.com/watch?v=v1MptV67kSI&si=IhISV4fNYZRUQmFU
**Title:** Claude Code's favorite tech stack
**Channel:** Theo - t3․gg
**Upload date:** 2026-04-29
**Saved at:** 2026-04-29T13:26:02.211218+00:00

```text
0:00 Hopefully at this point we can all agree
0:01 that tools like Claude Code are pretty
0:02 good at making real contributions to
0:04 real code bases. But what happens when
0:06 they have to make suggestions not just
0:08 about the code but about what tech you
0:09 use? Sometimes it gets it really really
0:12 wrong. This example in particular
0:14 horrifies me. Claude told the user that
0:16 Planet Scale had shut our service down.
0:18 This is unsafe by any definition.
0:19 Anthropic has made no effort to correct
0:21 the situation. Here we can see it very
0:23 confidently asserting that Planet Scale
0:25 shut down its database service in
0:26 January of 2025. That is a
0:29 hallucination. That is really bad. So,
0:31 it's not recommending good tools like
0:33 Planet Scale. What is it recommending?
0:35 There are some examples here, but in the
0:37 replies, I saw this really interesting
0:39 post. What Claude Code actually chooses.
0:41 This is a survey that Amplifying ran on
0:43 Cloud Code directly figuring out what
0:45 tools it will pick for various tasks,
0:48 database backends, all of these types of
0:49 things. And the results are fascinating.
0:52 In some ways, I'm impressed. In others,
0:54 I'm terrified. And overall, I think we
0:56 need to pay more attention to these
0:58 types of things because I'm regularly
0:59 surprised by just how many people are
1:01 learning how to code and are building
1:02 their first stuff just using tools like
1:04 Cloud Code and honestly not doing much
1:07 research at all. More and more the tools
1:09 that are recommended by things like
1:10 Cloud Code are going to matter. But at
1:12 the very least, we should dig into what
1:13 it recommends today. I got one
1:14 recommendation I want to cover first,
1:16 though. Today's sponsor. It feels like
1:17 everything about my stack is changing.
1:19 The editor I use, the technologies I
1:20 use, the way I build has shifted
1:22 fundamentally over the years. But
1:24 there's one thing that's kind of stuck
1:25 and I don't know why. That thing is
1:27 GitHub actions. And it feels like
1:28 they've only gotten worse over time. I'm
1:30 spending more time waiting for them. I
1:31 need to push my code to run them. And
1:32 when they fail, I have to copy paste
1:34 errors all around. Wouldn't it be nice
1:35 if there was something that was better,
1:37 faster, programmatically executable, and
1:39 something that your agents could
1:40 actually use? They sponsor Depot and
1:42 they already figured out how to make the
1:43 CI run faster, but they recently added
1:46 more because they rebuilt the CI from
1:48 scratch. If you're scared of changing
1:49 over, you don't have to. You could still
1:51 get 10 times faster GitHub actions by
1:53 changing the one line for the runner.
1:55 Probably should mention that it's
1:56 cheaper, too. You can also get the 40
1:57 times faster Docker builds without
1:59 having to change anything. But if you
2:00 want CI that's better if you want
2:02 definitions that make more sense, a
2:03 programmable engine that your agents can
2:05 run and do things in parallel with, you
2:07 definitely check out's new CI. I will
2:09 let you know in advance it's incredibly
2:10 difficult to move over. First, you have
2:12 to install a CLI that is so hard to run
2:15 one command and then you have to run
2:17 another thing. That's two things you
2:19 have to do. That's terrible. If you
2:20 can't sense the sarcasm, it's incredibly
2:22 easy to move over to Depot's new CI. And
2:24 one of the most annoying things about CI
2:26 is secret management. And thankfully,
2:27 they have that figured out too with
2:28 their secret and ver argument in the
2:30 same exact CLI. And most importantly,
2:32 and this is my favorite thing, you can
2:34 run a workflow without having to push
2:36 the code. It will just use the code that
2:38 you currently have in your local working
2:40 tree. It is amazing that GitHub doesn't
2:42 have this yet, and I can't live without
2:44 it now. Speed up your agents and your
2:45 builds at soyv.link/depo. I like how
2:47 Amplifying opened this here. Cloud code
2:50 is a new gatekeeper. When a developer
2:52 says add a database and lets Cloud Code
2:53 handle it, the agent doesn't just
2:55 suggest. It installs packages, writes
2:57 imports, configures connections, commits
2:58 code. The tool it picks is the tool it
3:01 ships. As more devs let Cloud Code
3:02 handle tool selection, the stacks it
3:04 chooses become the stacks. This is a new
3:06 distribution channel where a single
3:07 model's training data may shape market
3:09 share more than a marketing budget or a
3:11 conference talk. For tool vendors, if
3:13 the agent doesn't pick you, you're
3:14 invisible to a growing share of the new
3:15 projects. For devs, your default text
3:17 increasingly shaped by what the agent
3:18 knows, not what you research. And for
3:20 the ecosystem, understanding what AI
3:21 actually chooses is no longer optional.
3:23 It's competitive intelligence. This was
3:25 some AI written slop for sure, but
3:27 hopefully the rest is good research.
3:28 From my cursory scroll earlier, it
3:30 seemed really solid. I will also say
3:32 that I've been doing my own similar
3:33 research here, admittedly in a very
3:35 selfish way. One of the benchmarks I
3:37 spun up is upload thing awareness. This
3:39 is a benchmark I made in order to plug
3:41 my service upload thing which is the
3:42 best and safest way to add file upload
3:44 to your full stack web apps in
3:46 particular next.js builds. I wanted to
3:47 see which models recommend upload thing
3:50 when asked about adding secure file
3:51 uploads to your next.js app. So I made a
3:53 bench that measures this. It is not
3:55 cheap because it writes a lot and
3:57 percent write is does upload thing come
3:59 up as one of the options. And the really
4:01 interesting thing I noticed is as the
4:03 models got smarter they started
4:05 recommending upload thing more and more
4:07 consistently. Oof. Grock 41 fast's only
4:09 at 2/3 so far. This was a fun one. We'll
4:11 look at the results at the end. This is
4:12 going to be an expensive run, but when
4:14 we have that running, we'll look through
4:16 what Claude recommends in general
4:19 because I don't want to just plug my
4:20 stuff. The methodology of the test here
4:22 is actually really cool. They had four
4:24 different project types. They had three
4:26 different models. They tested, three
4:27 runs each across the 20 tooling
4:29 categories they were looking for. Each
4:31 prompt was an open-ended what should I
4:32 use with no tool names anywhere in the
4:34 input. So, here's the four projects. One
4:36 was called Task Flow. It's a Nex.js app
4:38 using an old version of next. TypeScript
4:40 and app router invoice tracker which is
4:41 vit react 18 and typescript data
4:43 pipeline which was fast API python 311
4:46 pyantic and deployctl which is using
4:48 node typescript and commanderjs. The
4:50 biggest find is that agents build
4:51 instead of buying in 12 of 20
4:53 categories. Cloud code frequently builds
4:55 custom solutions rather than
4:56 recommending third party tools. Custom
4:58 and DIY implementations account for 12%
5:00 of all the primary picks. 252 out of 273
5:04 making it the single most common
5:05 recommendation. And there's definitely a
5:07 default stack built in where agents pick
5:09 thirdparty tools. They converge on
5:11 Verscell, Postgress, Stripe, Tailwind,
5:13 Shad CNN UI, PNPM, GitHub actions,
5:16 Sentry, Resend, Zustand, as well as
5:18 stack specific picks like Drizzle if
5:20 you're using databases with TypeScript,
5:22 SQL model if you're using Python for
5:23 OMS, Next O for O, and Viest or Piest
5:27 for JS and Python testing. Next off, as
5:29 the recommendation is very interesting
5:31 because it's not even next off anymore,
5:32 it's OJJS. So that might be really old
5:34 and I'm a huge Zustan fan. So, I
5:36 appreciate that being there. Let's dig
5:38 in further. There are certain categories
5:40 that are fully locked like GitHub
5:42 actions owning CI/CD, Shad CN owning UI
5:44 components at 90% and Stripe owning
5:47 payments at 91%. Models agree 90% of the
5:49 time within each ecosystem. All three
5:51 models pick the same top tools in 18 of
5:53 20 categories when compared within
5:55 ecosystem. Only caching in real time
5:57 show genuine cross ecosystem
5:58 disagreement. The other three
6:00 disagreements are artifacts of mixing JS
6:02 and Python results. And one last
6:04 interesting piece is that context
6:05 matters more than phrasing. The same
6:07 category will have different results
6:08 across different repos. If you give the
6:10 same prompt to two different projects,
6:12 the recommendations will be meaningfully
6:13 different. But within a given project,
6:15 it'll stay stable across five different
6:17 phrasings of the prompt. 76% consistency
6:20 there. That's really cool. It is worth
6:22 noting that the three models they tested
6:23 were all models by anthropic. It was
6:25 Sonnet 45, Opus 45, and Opus 46. So they
6:28 did not test GPT models. Turns out they
6:31 already published the Codex comparison
6:32 too. So, we'll get to that near the end.
6:34 Here are the actual prompts they used.
6:36 How do I deploy this? I need a database.
6:38 What should I use? Add user off. What
6:40 testing framework works best with this
6:41 stack? Add O. Recommend whatever works
6:44 best for the stack. Apparently, the
6:46 fastest responses were when they were
6:47 asked about deployment, only taking 32
6:49 seconds, but O would take much longer at
6:51 245 seconds. Longer response times
6:54 correlate with higher custom and DIY
6:56 rates. The model spends more time when
6:57 it builds from scratch, like with O
6:59 realtime and payments, versus when it
7:00 confidently picks a tool like deployment
7:01 or CI/CD. They have a whole section of
7:03 what the study cannot tell you. Probably
7:05 worth reading for people who are going
7:06 to read into this too much. I like the
7:08 call outs here. It's not developer
7:09 consensus. They cannot separate quality
7:11 signals from training frequency. They
7:13 don't have any special insight here.
7:15 This is just an interesting deep dive
7:17 into what the models like and recommend
7:19 and to some extent how they think. One
7:21 last interesting call out here is that
7:23 when cloud code doesn't recommend
7:25 things, it's usually because it was
7:27 asking additional questions. Claude Code
7:29 is often cautious, not confused. asked
7:31 clarifying questions or requested
7:32 permission before proceeding. Sometimes
7:34 I misunderstand the prompt, but it
7:35 wasn't very common. Certain features
7:36 like feature flags and background jobs
7:38 would trigger caution more often than
7:40 others. And now we get into the results.
7:42 First, we have the custom in DIY
7:43 section. Cloud Code frequently prefers
7:45 to build custom solutions rather than
7:47 recommend third party tools. When asked
7:49 to add feature flags, it doesn't say use
7:51 launch darkly. It builds a complete
7:53 feature flag system from scratch using
7:55 environment variables and framework
7:56 primitives. This one's particularly
7:58 funny as an example because Claude Code
8:00 doesn't do that. Cloud code is using
8:01 stats sig both for doing stats and like
8:04 product analytics stuff but also for
8:05 feature flags. They were but then stats
8:08 say got acquired by open AAI. So cloud
8:10 code moved over to growth book. And when
8:12 I say cloud code moved to growthbook, I
8:13 mean that the team building cla moved
8:15 cloud code itself to growth book. So
8:18 even though cloud code likes to DIY
8:20 feature flags, cloud code itself does
8:22 not use DIY feature flags. Just thought
8:24 that was funny. So the recommendations
8:26 Cloud Code makes are not the
8:27 recommendations that Enthropic follows
8:28 for building Claude Code. So to
8:30 everybody saying the models are clearly
8:31 dumb. If they leaked the Cloud Code
8:33 source, the models didn't leak the
8:34 source. The developers did. And the
8:36 developers don't just blindly trust
8:38 whatever Claude does. As mentioned
8:39 earlier, if custom and DIY counted as a
8:42 tool, it would be the most common one
8:43 across everything. 70% of the time
8:45 feature flags were requested, a DIY
8:47 solution would be used. 100% of the time
8:49 off was requested in Python projects,
8:51 DIY would be used. Overall though, only
8:54 half the time would it use DIY for O.
8:57 Observability was a lot lower at 22%,
8:59 email also low at 22%. Please do not
9:02 roll your own SMTP integrations. It is
9:04 hell. Use any of the services. I'm not
9:06 sponsored by any of them right now.
9:08 There's a lot that are good. Resend is
9:10 popular for reasons. There's also plenty
9:11 of other options, too. I like the Loops
9:13 guys a lot. Do not roll your own email
9:16 unless you know what the hell you're
9:17 doing. It is pain. Speaking of things
9:19 that are pain, real time, man, I've been
9:23 through it with real time and sync
9:25 engines. You can do it, but if you have
9:27 never had to debug frames coming through
9:29 a websocket on the client side, you
9:32 probably should use something else for
9:33 this. It's not fun. There's a reason
9:35 it's only 21% of the time it's diying
9:38 it. But yeah, forms are down to 20% of
9:41 the time. Using custom React hooks and
9:42 use state validation instead of using a
9:44 form library. Cachings at 19% will be
9:47 diyed. styling 17% DIY. The models
9:50 really like using Tailwind and Chad CNN.
9:51 And then file storage is only at 12%.
9:54 Very interesting. Speaking of file
9:55 storage, how's my bench going?
9:56 Interesting so far. I need to add 5.4 to
9:58 this at some point, too. A good call out
10:00 here is why this matters for tool
10:02 vendors. If coding agents are becoming
10:04 the default way developers discover
10:06 tools and the agents prefer building
10:07 over buying, vendors need to either
10:09 become the primitive that agents build
10:10 on or make the tools so obviously
10:12 superior that agents recommend them over
10:14 custom solutions. It's funny that's
10:15 mentioned because I saw this post from
10:17 Mitchell earlier today. If you're not
10:18 familiar with Mitchell, he is the
10:20 creator of Terraform and Hashi Corp and
10:21 he's also the creator of Ghosty and more
10:23 importantly Liby. He wrote an article
10:26 today about the building block economy.
10:28 The most effective way to build software
10:29 and get massive adoption is no longer
10:31 highquality mainline apps, but via
10:33 building blocks that enable and
10:34 encourage others to build quantity over
10:36 quality. So Ghosti got to 1 million
10:38 daily users in 18 months. Lib Ghosty,
10:40 the library that you can use to build
10:42 your own terminal integrations with
10:44 Ghosty's backend, gets multiple millions
10:46 of daily users already in just two
10:47 months. And there's lots of other
10:49 projects that are seeing this type of
10:50 success due to the building block
10:51 nature. I don't want to spoil the
10:53 technologies yet, but I thought this
10:54 article was worth calling out. I'll
10:55 leave the link in the description. I
10:56 will also be doing a whole video about
10:58 this in the business side of open source
10:59 and building blocks in the near future,
11:00 so keep an eye out for that. Back to the
11:02 tool rankings. Here's the overall. Oh
11:04 boy. GitHub Actions has a near monopoly
11:06 at 94%. Stripes also near Monopoly at
11:09 91.4%. Shad CNUI is at 90%. Versel's at
11:12 100% for JS which is insane. Tailwind is
11:15 at 68.4%. Zustan's also matching that.
11:18 Kind of crazy that Tailwind and Zustan
11:19 are similarly popular. I love Zustan,
11:21 but seeing it become this prominent is
11:23 insane. I never thought it would even be
11:25 a tenth as popular as Redux, but that
11:28 flipped quickly. Yeah, Redux is at 21.5
11:31 million installs per week right now. And
11:33 Zustin's at 22. Holy [ __ ] It happened.
11:36 It happened. Zustand is more popular
11:40 than Redux. I never thought I'd see the
11:42 day. I might have to start pronouncing
11:43 it properly out of respect. I will never
11:45 do that. It is Zustand forever. So yeah,
11:47 Zustand is much more popular than I ever
11:49 thought it would be. Still really cool
11:50 to see. It's crazy seeing it above
11:51 Sentry cuz like there's a reason that
11:53 Sentry is so popular. They are still the
11:55 most complete bug tracking solution for
11:58 error management in real software,
12:00 especially mobile. Going down the list
12:02 further, we got Reend. As I mentioned
12:04 before, please don't roll your own email
12:06 solutions. B test which is really good
12:08 for doing testing in Typescript. I'm so
12:10 thankful we're not getting like old
12:12 tools like just in here. Postgress is
12:14 the main database pick. I have my
12:15 opinions. Postgress is fine. But if your
12:18 project grows, you got to know how to
12:20 scale Postgress and the consequences of
12:22 the choice. I find that if you're not
12:23 having to worry about scale, SQLite's a
12:25 pretty good option. If you are, my SQL
12:27 is still the undefeated goat. Especially
12:29 if you use a platform that can handle
12:31 that with Vitess, which isn't vitest.
12:33 Vitas vits is a way to scale my SQL.
12:36 Planet scale has it handled really well.
12:37 Highly recommend it. Postgress is a
12:39 weird in-between that I don't find
12:40 myself recommending a lot, but it's
12:42 fine. As many of you all know, I prefer
12:44 integrations with my database that go a
12:45 little deeper in terms of how it relates
12:48 to my backend as well as my client. And
12:50 I really like Convex for that
12:51 specifically. We got PNPM here at 56.3%.
12:54 React hook form great library at 52%.
12:57 Tanstack form is catching up now in
12:59 functionality, but React Hook Form is
13:01 the undefeated goat still. Reddus is at
13:03 41.6. Tanstack query is only at 40%.
13:06 That's a bit sad to see. This should be
13:08 a lot higher. One of the fun things I
13:09 noticed is that a lot of people who have
13:11 historically not been too deep on the
13:13 front end in React side because they're
13:15 building bigger apps now and they're
13:17 using tools like Cloud Code to do the
13:19 front end a little deeper. Somebody like
13:21 Aaron who comes from the PHP world is
13:23 suddenly really deep in dynamic
13:25 front-end application development and
13:27 just discovered Tanstack query and how
13:28 great it is. And it's very cute seeing
13:30 all these people discover Tanstack query
13:32 six plus years after I started
13:34 evangelizing it. And over on the Python
13:36 side, we have fast API makes a lot of
13:38 sense. AWSS3 is very competitive for
13:40 file storage, but it's only at 32.5%.
13:43 That's very interesting. I want to see
13:45 the other file storage solutions. Next
13:47 off is pretty low at 31. Next.js API
13:50 routes is also weirdly low at 28.6%.
13:52 Piest is 25.7. Actually on the nextJS
13:55 routes one. I wonder if that's because
13:57 there are other apps that aren't using
13:59 next. So this is just recommended in the
14:01 next.js instances. And then railway is
14:03 on the list but barely at 25.6%.
14:06 Cool. So far let's compare the different
14:09 categories with CI/CD. GitHub wins by
14:12 far. Verscell CI is recommended which is
14:14 funny. I don't even really recommend
14:15 VerselCI beyond building. I turn off all
14:17 the checks in VerselCI. I just let it
14:19 build and I run my actions for all my
14:22 type checking and whatnot. I usually use
14:24 something like Depot, Blacksmith or RWX
14:26 in order to be much faster and less [ __ ]
14:28 than GitHub actions. This is also funny
14:30 because I happen to know that all those
14:31 companies I just mentioned are doing
14:33 very well stealing a lot of customers
14:35 from GitHub actions. So I don't know how
14:37 long term this will stay, but this is
14:39 absolutely the case now. Then we have
14:41 payments where Stripe is by far the lead
14:43 at 91.4%. Custom DIY is at 8.6. And then
14:47 there's a few other times that Paddle,
14:49 Lemon Squeezy, and PayPal were
14:50 recommended. We're using Autumn now for
14:52 T3 chat. I invested in them forever ago.
14:55 Didn't think it was the right solution
14:56 for us and then Mark started talking to
14:58 the team and despite the fact that Mark
15:00 almost never recommends solutions that
15:02 are newer, he ended up really liking
15:04 Autumn. So that's what we're using now
15:06 and it's been a nice change for us. And
15:08 then we get into UI components where
15:09 Shaden sweeps. Radex UI is a little
15:12 behind, but remember that Radex is also
15:14 a core depth for Shaden. So most people
15:16 just go Shaden. Shakra, Mantine, and
15:18 Material all appeared as alternatives,
15:20 but they were rarely the primary
15:21 recommendations. Makes sense. And then
15:23 deployment, mostly Versel at 76.8%
15:27 and Railway at about 28.6. Interesting
15:29 to see Railway get recommended so
15:31 heavily. It makes sense when you see
15:33 their user growth recently. I almost
15:35 started working at Railway even before
15:38 this. Yeah, we were in talks back in
15:39 2021 and Jake convinced me to go do my
15:42 own company instead. It would have been
15:43 the fourth employee at the company if I
15:45 recall and I declined it because
15:47 actually funny enough he told me that I
15:49 should probably make my own thing. So I
15:50 did but seeing this after is insane.
15:53 Like they're at over 15,000 new
15:56 deployments a day I think or new users
15:58 per day. 15k new users a day on a dev
16:00 tool is insane. And that lines up here.
16:02 That makes a lot of sense. What's really
16:04 interesting here is the ecosystem note
16:06 where 100% of the time it was asked for
16:08 JavaScript it picked Verscell but for
16:10 Python railway was usually picked but
16:12 only at 82%. It is also worth noting
16:14 that Verscell has a free tier and is
16:16 pretty damn scalable. Railway doesn't
16:18 have a free tier so it being this
16:20 popular is an interesting thing. And to
16:22 be clear with Railway they let you get a
16:24 little bit of usage every month for
16:25 free. I think it's like five bucks or so
16:26 but that's barely enough to keep a
16:27 server live the whole month. I also use
16:29 Railway heavily for side projects and it
16:31 cost me almost nothing. They are
16:32 hilariously cheap. They're often cheaper
16:34 than AWS, which is just insane. Turns
16:36 out running your own hardware is
16:37 powerful. AWS Amplify was mentioned 24
16:39 times, but never recommended as a
16:41 primary or alternative. Claude, we are
16:44 aligned. [ __ ] Amplify. I [ __ ] hate
16:46 Amplify. I was one of the earliest
16:47 testers of Amplify when I was at Amazon.
16:49 It was such a [ __ ] show. Such a [ __ ]
16:51 show. Netlifi was recommended as an
16:53 alternative 67 times. Render was
16:55 recommended 50 times. Fly was only
16:57 recommended 35. Cloudflare pages was 30.
17:00 But cloud page is also kind of dead
17:02 because it's part of workers now whole
17:04 thing and GitHub page is only 26 times.
17:06 Interesting to see how much these falter
17:09 also that Netlefi is almost twice as
17:11 highly recommended as fly and more than
17:13 twice as highly recommended as
17:14 Cloudflare pages. That says a lot. And
17:16 now we get into the strong defaults
17:18 things that have over 50% but aren't
17:20 quite in the monopoly tier. For styling,
17:21 Tailwind absolutely crushes at almost
17:23 70%. Custom DIY is the next highest at
17:26 17 and then CSS modules is at 13%. Style
17:29 components emotion and SAS were nearly
17:30 absent from primary picks. However, CSS
17:33 modules got 42 alt picks and style
17:35 components appeared 14 times as an
17:36 alternative and was mentioned 35.
17:38 Interesting. For state management,
17:40 Zustand was super popular and tanstack
17:43 query less. So like if you're doing
17:44 client state, Zustand makes a ton of
17:46 sense. But if you're doing server state
17:48 where you're fetching data and showing
17:49 it in the UI, having mutations that
17:51 trigger asynchronous stuff, tan stack
17:54 makes a lot more sense for anything that
17:56 is like a this rendered and I need data
17:58 type thing. And React context being solo
18:00 is kind of hilarious. Yeah, I would
18:02 really want to see the prompt they're
18:03 using for this test. We then get to
18:04 observability where Sentry sweeps.
18:06 Customdy is at 20%ish, but Sentry more
18:09 than triples, which is crazy. Prometheus
18:11 is at 12 out of 160, so at 7 and a half.
18:14 And then Pino, which I've never heard
18:15 of, at 6%. Email has resend sweeping
18:18 then customdy at 20% and then send grid
18:20 way behind at seven. Testing v test
18:22 crushes pi test is pretty high.
18:24 Playright which is an interesting thing
18:26 to sneak in here is doing okay at 10%.
18:28 But playright is really for testing in
18:30 the browser not just for running your
18:32 tests. Seems like the vagueness of the
18:34 prompt has steered the model into saying
18:36 lots of other things. And then there's
18:37 just which is at 4% where it belongs the
18:40 bottom. I will never ever miss jest.
18:43 Databases as I mentioned before
18:44 Postgress is crushing at 58%. Superbase
18:47 is still in my opinion higher than it
18:48 should be at 24%. My gripe with
18:50 superbase is specifically that so much
18:52 of the state lives in the existing
18:54 database and not in your codebase.
18:56 Things like the permission system and
18:58 model, things like the current state of
19:00 the database, what migration level it's
19:03 at, all these things exist in the
19:06 database itself. And you have to use an
19:08 MCP in order to keep the database in the
19:10 right state as you're working with it.
19:12 On top of that, the off model is
19:14 something you have to put effort into.
19:16 Rowle security is far from my favorite
19:18 way to handle safe application
19:20 development. So, Superbase not a
19:22 recommendation I make a lot. I suspect
19:24 this one will drop over time. But I also
19:26 think Superbase is going to work hard to
19:28 unfuck their things because they have
19:29 way too much state living in their
19:30 dashboard and way too little living in
19:32 the codebase. And then SQLite because
19:34 who doesn't love a good meme? [ __ ] got
19:36 zero primary picks but was heavily
19:37 mentioned. Models know it, they just
19:39 don't default to it. Interesting.
19:41 Overall, I am sad to not see my favorite
19:43 Convex here, but I get it. Convex is
19:46 still a new thing. I'm sure the models
19:47 will recommend it more in the future.
19:48 Then we got package managers. I am Oh, I
19:51 was happy with the results until I saw
19:53 how high npm was. PNPM is the top
19:55 choice. I think this makes a lot of
19:56 sense. Bun is great, but it has edges
19:59 that can make it annoying for lots of
20:01 projects, especially mono repos. We've
20:03 had enough bugs with bun and T3 code,
20:05 even just for our package management
20:06 that we're considering moving off. Also
20:08 funny cuz bun is owned by Anthropic but
20:10 it's still third place here. PNPM still
20:12 sweeps here at 56.3% and then npm is at
20:15 23%. Please stop using npm for package
20:17 management. Just use pnpm or bun. Also
20:20 probably not worth picking yarn
20:21 nowadays. Now we're in forms. One of my
20:24 favorite topics. React hook form is at
20:25 50%. Zod is at 26.7%. Zod's not for
20:29 forms though. It's just validation. And
20:31 apparently it appears as standalone
20:33 validation pretty often alongside I'm
20:35 assuming the custom DIY implementation.
20:37 Please validate your forms. Zod's a
20:39 really good option for it. And now we're
20:40 into competitive markets where nothing
20:42 has more than 50% dominance. Eight
20:44 categories and no clear winner. For O
20:46 customdy is just barely under 50%. Next
20:50 off does pretty well at 31% and then
20:52 superbase offs at 11%. Next off is
20:54 recommended 91% of the time for next.js
20:56 which is interesting. So remember next
20:57 off doesn't really exist anymore. you're
21:00 supposed to just use ojs, but it's been
21:02 folded in as part of better off. Like
21:03 it's all into better off now. Like,
21:07 yeah, it's interesting seeing it
21:09 recommended so much when it's like part
21:11 of better off. Yeah. Wild. That that
21:14 shows you that these models are all old
21:15 data. Convex off is getting mentioned in
21:17 my chat. Personally, I don't love it.
21:19 And funny enough, Convex doesn't either.
21:20 They highly recommend at Convex that you
21:22 use other o solutions. Personally, I
21:24 really like both clerk and work OS. Both
21:26 are easy recommendations. Better off is
21:28 also in a really good state nowadays.
21:29 For what it's worth, I'm annoyed enough
21:31 with Oth that I'm building my own O
21:32 service that I'm hoping, fingers
21:34 crossed, to get out soon. Still
21:35 polishing a few things. It is out. If
21:37 you want to try it, be cautious. It's
21:39 not open source yet. And apparently,
21:40 there are some things in it that might
21:41 not be the most secure. We're working on
21:43 it. I'll get it out soon. I'm very happy
21:44 with it. Now, we have caching with
21:46 Reddus doing very well at 41.6% probably
21:49 where that belongs. Custom DIY at 19.5
21:52 and Nex.js JS's built-in cache, which to
21:54 be clear is built in, but it's built in
21:57 in a way where you need to host it on a
21:59 platform that understands how to use it,
22:00 which means you're probably on Versell.
22:01 It's really versel's cache, I would
22:03 argue, but 20% overall is not bad, but
22:06 in Nex.js apps, it got recommended 42%
22:08 of the time. And in Python, Reddus did
22:10 break out over 50 to 57%. Very split by
22:13 the stack. Makes sense. Again, it's
22:14 really cool to see that the stack that
22:16 your project is in when you run the
22:17 prompt really helps determine where
22:19 things go.
22:21 And now we're in the API layer section.
22:24 Very interesting to see Tanstack only at
22:26 40% here. Fast API at 35 and next API
22:29 routes at 28.6 because none of these are
22:32 competitive with each other. I've seen
22:34 projects that use all of these.
22:36 Thankfully, even though none of these
22:38 conflict, Tanstack does get recommended
22:40 much more heavily for React projects at
22:41 70% of the time. I would say it should
22:43 be more than that. It should be near
22:44 100, but it's good to see. Python has
22:46 fast API 100% of the time and next has
22:49 API rest recommended almost 80% as well.
22:52 This is very stack determined. And now
22:53 we have file storage. Um sir, where's my
22:57 mention? According to them, I'm not even
23:00 on the list, but we look at my research
23:01 here. Most of the models are at least
23:03 aware of upload thing and will recommend
23:04 it as an option. Every modern claude
23:07 model is willing to. Sonet 46, Opus4 5,
23:09 and Opus 46 recommend upload thing 100%
23:11 of the time. Also worth noting that
23:13 benchmark cost me $22 to run. Well, if I
23:15 got to spend all this money to figure
23:17 out how popular upload thing is, we
23:19 should probably take a break for another
23:20 really good recommendation from today's
23:21 sponsor. AI has made our lives much
23:23 easier. As long as you're using it for
23:25 code, as soon as you have to do
23:26 something else, like hiring, AI actually
23:28 makes your life much worse, because all
23:29 of a sudden, we're all getting spammed
23:31 with endless applications from people
23:32 that don't necessarily know what they're
23:34 doing, filling their resumes up with AI
23:36 generated slop. Hiring sucks so hard
23:38 right now, and recruiters just don't
23:40 know what they're doing or how to deal
23:41 with it. All the signals they used to
23:43 rely on to make good hiring decisions
23:44 just don't really work anymore. And
23:46 that's why G2I is such an easy
23:48 recommendation for all the companies I
23:49 know who are trying to hire. They don't
23:51 base hiring decisions off of sloppy
23:53 resumes. They already have a network of
23:55 talented engineers. Every time I talk to
23:56 somebody at G2I, I'm impressed with the
23:58 depth at which they understand the
24:00 people. Just a silly example, I recently
24:02 reached out to them on behalf of a
24:03 company I was trying to help with
24:04 hiring. That company had a CEO that
24:06 really knew the industry and was trying
24:08 to pick the best possible people. So, I
24:10 assumed that they wouldn't need much
24:11 help, but I figured I'd throw them in
24:13 the ring anyways. What really blew me
24:14 away was that G2I responded with a list
24:16 of awesome candidates and like
24:18 descriptions where they clearly
24:19 understood who the person was and what
24:21 they did. And three of the candidates on
24:22 their list were friends of the CEO. The
24:25 depth of their network is insane. And
24:27 that's why companies like Web Flow, One
24:28 Password, Automatic, and even Meta have
24:30 worked with them for hiring. It's their
24:32 goal to go from interview to first PR in
24:34 7 days. and have seen them do it enough
24:36 times to recommend them with confidence.
24:38 Stop suffering with hiring and get back
24:39 to building at soy dev.link/g2i. God,
24:41 it's doing so many tokens. It's 5 cents
24:43 per run on this one. Jesus Christ. 3k
24:46 tokens. Well, hopefully we'll get 100%
24:48 there. This is taking a while, but so
24:50 far 5.4 is at 100%. So again, as the
24:53 models get smarter, they are more likely
24:54 to recommend upload things. So take that
24:56 as you will. If you want to be as smart
24:58 as the smartest models, maybe use my
25:00 stuff. I'll come back and look at the
25:01 final results later though, I promise.
25:03 Back to very competitive categories like
25:05 OMS and database tools where SQL model
25:07 and Drizzle are the highest. Prisma is
25:09 not too far behind and SQL Alchemy is a
25:11 little behind there. In Python, SQL
25:12 model is at 72% though and in JS Drizzle
25:15 is at 61% and next. So yeah, Drizzle is
25:18 doing very well. Congrats to the Drizzle
25:19 team. Background jobs has BMQ near the
25:22 top, but it's only at 25%. Ingest is
25:25 right behind it at 23%. Celery is at 18.
25:28 Fast API is at 13. Also split by
25:30 ecosystem a good bit. I will say I'm
25:32 surprised to not see Trigger here. I
25:34 know they're a sponsor, but Trigger is
25:35 awesome. My whole team has been super
25:37 impressed since we started playing with
25:38 it more. Definitely worth checking out.
25:40 I actually owe them some ads. I just
25:41 realized I will be hitting them up soon.
25:43 Uh yeah, Trigger's been they're too
25:45 chill to work with. You would have heard
25:46 about them a lot more if they were less
25:48 chill, but they're very cool with me
25:49 being late. And as soon as I mentioned
25:51 Trigger, chat's like, "Oh my god,
25:52 Trigger is amazing. Trigger's awesome."
25:54 Yeah, they're really, really good. And
25:55 now we're in feature flags where they
25:57 overrecommend custom and DIY. Launch
25:59 Darkly's in second place at 20% and Post
26:01 Hogs all the way back at 4%. We use the
26:04 Post Hog feature flags. They're pretty
26:05 dang good. Growth book is awesome, too.
26:07 I'm surprised they're not mentioned here
26:08 at all, especially because they use
26:10 growth book inside of Cloud Code. And
26:12 then real time custom DIY at 20%,
26:15 Superbase at 15, SSE at 14, socket io at
26:18 11, Live Blocks also gets mentioned for
26:20 collaboration, but yeah, no clear winner
26:23 here. And now we're in the model
26:25 comparison section. Not comparing with
26:26 codecs. We'll get there right after. But
26:28 just seeing how the recommendations
26:29 break down depending on the new versions
26:31 and old versions of the models. GitHub
26:33 actions went down significantly from 45
26:35 to 46 which is interesting. Postgress
26:38 got a little more popular. Versel got
26:39 less popular. Interesting. Resend is
26:42 plummeting. Sonnet had 84. Opus 45 was
26:45 77. And Opus 46 is 66. That's actually
26:48 very interesting. PNPM hit a straight
26:50 100 across all three. Stripe was 73
26:54 8376.
26:55 Zustand got to 100% with Opus 46.
26:57 Interesting. Tailwind was only 100% for
27:00 Opus 45. Fascinating. I wouldn't read
27:03 too much into these simply because the
27:06 models are all similar and this is all
27:07 non-determinism. So yeah,
27:11 apparently Drizzle's 100% on Opus 46,
27:14 but Prisma is more popular on Sonnet 45.
27:17 This is very interesting to see which
27:19 times they disagree. The rest aren't
27:21 anywhere near as big a split. Actually,
27:23 Reddus was much more popular Sonnet 45
27:25 than Opus 45, which is fascinating. One
27:27 of the other really interesting things
27:28 is that Prisma dropped from 79% with
27:30 Sonnet to 0% with Opus 46 and Drizzle
27:33 rose from 21 to 100%. One more fun
27:36 observation is the recency gradient
27:38 within each ecosystem. Newer models pick
27:40 newer tools. All percentages below are
27:41 within ecosystem. For example, Prisma
27:44 79% is 79% of the JS. Okay. Yeah. Very
27:47 interesting to see the difference there.
27:49 And it seems like, interestingly enough,
27:51 the newer models, especially the newer,
27:53 smarter ones like Opus, are more willing
27:55 to try out new tools and go in that
27:57 direction. Where with Sonnet 45, it
28:00 tends to fall back on existing
28:01 established popular things and not
28:04 trying to go with the new stuff. It's
28:06 also less willing to build custom
28:07 solutions, which is interesting. Yeah,
28:09 fascinating. So, we wanted to summarize
28:11 the most frequently picked things in
28:13 cloud code in these scenarios. It would
28:15 be resend for email, vest over just,
28:18 PNPM is the package manager, Drizzle,
28:20 Shad CN, and Zustand are all the most
28:22 popular options. Now, let's see how
28:24 Codeex compares. I'm actually really
28:25 curious here. The top here is very
28:28 interesting. They list all of the
28:29 different specific categories and what
28:32 the number one pick was between the two.
28:34 And there's a lot of agreement overall
28:36 in particular when a lot of the DIY
28:38 stuff is being recommended. But when it
28:39 comes to something like scheduled tasks,
28:41 codeex recommends OS level cron and
28:44 cloud code recommends something like
28:45 versel in their cron implementation. For
28:47 search, cloud code likes postgress. For
28:50 js runtime, codeex prefers node and
28:52 cloud code prefers bun. Surprise, that
28:55 is actually genuinely surprising and
28:56 very interesting. And for edge and
28:57 serverless, cloudflare workers is
28:59 preferred by codeex and verscell edge is
29:01 preferred by cloud code, which is
29:03 interesting because verscell edge is
29:04 pretty dead. It's your like edge on
29:06 Verscell is not what you should use
29:07 Versell for. You should use it for their
29:09 like fluid compute model with that's
29:11 serverless but isn't really serverless.
29:13 Interesting. Also, the gap in the
29:14 recommendation level here where
29:16 Cloudflare workers recommended by Codeex
29:17 50% of the time and Verscell's Edge is
29:19 only recommended 24% on Cloud Code,
29:21 meaning there isn't a real number one
29:23 winner there. It also looks like they
29:24 might have hardcoded statig out on
29:26 Claude because they're mad about them
29:28 being bought by OpenAI because Claude
29:30 never recommends it even though they
29:31 were using it and Codex recommends it
29:33 over a fourth of the time. So that's an
29:34 interesting gap. The ownership question.
29:36 This is funny because both have this
29:37 problem where stat sig is no longer
29:40 recommended by claude code because
29:43 probably not really but potentially
29:45 because openai bought them where with
29:46 bun codex doesn't recommend it anywhere
29:48 near as much but cloud code does a lot
29:49 of the time and almost always mentions
29:51 it. Another fun gap when asking
29:53 specifically about AB testing and
29:54 feature flags. Codex picks statig and
29:56 cloud code picks post hog. Very
29:58 interesting. Oh, before I forget, what
29:59 about upload thing? The uh 5.4 24 Pro
30:02 runs are uh not resolving. I think it's
30:05 cuz I have a timeout on them and they
30:07 take longer than that. So, I probably
30:08 just spent a lot of money and will never
30:10 get the results, which is annoying.
30:11 Might have to bump the timeouts up.
30:13 Regardless, 5.4x high got 100% upload
30:17 thing recommendations. So, again, as the
30:18 models get smarter, they recommend what
30:19 I build. I know this seems like I'm just
30:21 plugging upload thing really hard. It's
30:23 cuz I am, but it's also because it makes
30:24 jack [ __ ] [ __ ] for money. The free
30:26 tier is too generous and the paying
30:28 users don't pay a whole lot. So this is
30:30 like we lose two grand a month on upload
30:32 thing right now. It's not a big
30:33 profitable service. I just put a lot of
30:35 work into it and care. Oh, this is
30:37 actually very interesting. Claude code
30:38 is just wrong with the bun
30:41 recommendation here. When they start the
30:43 project is on node by default, but they
30:45 ask what JavaScript runtime should be
30:47 used for the project. Is there something
30:48 faster than we have? And this is a
30:49 next.js14 project. Remember next cannot
30:53 run in bun. Next is not compatible with
30:55 bun. has a bunch of weird async IO stuff
30:58 that is node specific that is not
31:00 implemented in bun. This is just wrong.
31:02 Install times is correct. Sure, it's
31:03 faster than npm, but we're not asking
31:05 about the [ __ ] install times. We're
31:08 asking about bun rundev and the runtime
31:10 for this. Bun would be the fastest
31:12 runtime option for next 14. This is just
31:14 wrong. That is a lie. Just saying. Next
31:16 is tightly coupled to node internals. So
31:18 while bun works well for install and
31:19 dev, the actual next server still runs
31:21 on node under the hood. TLDDR use bun
31:23 for speed. fall back to PMPM if you hit
31:25 compatibility issues. On a question
31:26 about runtimes, it's saying what package
31:28 manager you should use. Opus is really
31:31 smart until it's really stupid and then
31:32 it's really [ __ ] stupid. And this is
31:34 an example of it being really dumb. The
31:36 way I described this to somebody
31:37 yesterday is when I use claud code and
31:40 opus, it kind of feels like the prompt
31:42 you give it isn't so much an instruction
31:44 as a word cloud and a vibe that you want
31:47 it to feel out. So when it got the
31:49 prompt of what JS runtime should I use
31:51 that gave it the vibe of things like
31:53 node and bun and that gave it the
31:56 additional vibe of things like pnpm and
31:58 package managers and then you got an
32:00 answer about package managers even
32:02 though the question is about run times
32:03 whereas with open AAI models in
32:05 particular 5.3 codex and 5.4 it feels
32:08 more like you're telling the model what
32:09 to do and it follows it as instructions
32:11 sometimes too literally. So here we get
32:14 a much much better answer like like the
32:15 gap in the quality of the answer here is
32:17 insane. What you have today is nodebased
32:19 and that is still the safest path for
32:20 next compatibility. It also opens
32:22 specifically saying keep node as your
32:24 primary runtime for this project. It
32:25 immediately answers what the question is
32:27 and then gives you some additional
32:29 information that is very specific. If
32:31 you want faster lowrisk speed up that's
32:33 recommended is that you stay on node
32:35 runtime. The first thing it says but you
32:37 also switch tooling to pnpm or bun
32:39 install for faster dependency installs.
32:41 Runtime experiment. Bun can be faster
32:43 for startup and CPU heavy work, but for
32:45 next on Verscell, it's still marked as
32:46 beta as of November 10th, 2025. So, use
32:49 staging first. Okay, so apparently there
32:50 is a beta runtime for bun with next on
32:52 Verscell. I didn't even know that. Cool
32:54 to learn a thing. I I vaguely remember
32:56 this happening, but calling it out
32:58 properly. And the biggest practical next
33:01 speed gain is to upgrade from 14 to 16
33:03 where turbo pack is the default, which
33:04 will improve your dev and build
33:05 environment. Also, node release guidance
33:07 now shows v24 is active LTS and
33:10 recommends active and maintenance LTS
33:11 for production. So target node 24 for
33:13 prod and then it links all of the
33:14 sources that it used. Do you understand
33:16 the gap in that quality of response? I
33:18 don't even care what it recommends. I
33:19 care that it actually understands what
33:21 it's recommending and writes it out
33:22 properly. This test about platform
33:24 preference doesn't appear to be the best
33:27 because they're asking about edge
33:29 compute. And this is also just a bad
33:31 prompt. Like you don't actually want to
33:32 run code close to the users because the
33:34 code needs data and the data is probably
33:36 centralized. I have a lot of videos
33:38 about this. But if you really want
33:40 compute near your users, you got to go
33:42 with Cloudflare. It's the right option
33:44 here. But the in the Verscell Edge stuff
33:46 is just not their focus anymore. They've
33:48 even come out against it like formally.
33:50 Just no. This this prompt is bad and
33:53 OpenAI codeex followed the intent of the
33:56 prompt correctly and Claude Code doesn't
33:59 understand what's going on here and
34:00 didn't do the proper research. I'm
34:02 actually curious if either mentioned the
34:03 fact that you need your data close to
34:05 the code. Let's see. None of them do.
34:09 I've got into some arguments with some
34:11 very early into coding people that are
34:13 like learning how to code through vibe
34:14 coding that very strongly asserted that
34:17 my takes on like I think it was my
34:19 convex takes were wrong because convex
34:21 doesn't have an edge compute platform
34:23 and superbase does. Yeah, it's the
34:24 database. You want the compute next to
34:26 the database. The more it has to travel
34:28 the worse it is. I have a lot of videos
34:29 about this. Look up theo edge and you'll
34:30 find a ton of them. I would like for the
34:32 models to tell you about that. Codex
34:34 calls out that Verscell has an edge, but
34:36 the docs now recommend moving many edge
34:38 workloads to node runtime for
34:39 performance and reliability. Correct.
34:42 God, it's funny that neither really
34:45 recommend growth book. They've only
34:46 mentioned it even once even though Cloud
34:48 Code is using it. And then JS runtime
34:50 and tool chain pretty big gap. Vest is
34:52 more popular with cloud code. It's still
34:54 recommended over here. PNPM does much
34:57 better in the codec side than on the
34:59 Cloud Code side overall, but both are
35:00 recommended pretty heavily. Interesting.
35:02 It looks like Cloud Code just never
35:04 recommends Cloudflare. Cloudflare images
35:07 got a huge wreck on Codeex side, but it
35:09 didn't get even listed on the Cloud Code
35:11 side. Image optimization is obnoxious.
35:13 So, yeah, I don't I totally understand
35:16 why somebody would ask the models and
35:18 I've been through it with that. Image
35:19 Kit was really good for my experience. I
35:20 like them a lot. Was it Bunny CDN? Yeah,
35:23 I was trying Bunny. It's pretty well
35:25 priced and good, but god, it sucked so
35:27 hard to set up. Like, so insanely hard.
35:30 Next, image is a good recommendation now
35:31 that Versell made it cheaper especially,
35:32 but Cloudflare images is also pretty
35:34 good. Just a little more code you have
35:35 to write. Also can be a little hard to
35:36 secure on the Cloudflare images side.
35:38 I've ranted at them about that in the
35:39 past. Headless CMS's good bit of
35:42 disagreement, but who cares? They're
35:43 headless CMSs. You can vibe code your
35:45 own alternative at this point. Why would
35:46 you ever DIY SMS? That's insanity.
35:50 Codeex, come on guys. What service
35:51 should I use to rate limit and protect
35:53 my API in prod Cloudflare is 20% on the
35:56 codec side and it's only 8% on the Cloud
35:59 Code side. Weird that Claude doesn't
36:00 like Cloudflare so much. It's very
36:01 interesting to see some cool companies
36:03 called out as cross agent picks that are
36:05 up and coming. Doppler is doing pretty
36:07 well. Upstach is doing pretty well. Our
36:10 friends over at Axium are doing very
36:11 well. And Melee Search is also doing
36:13 well, too. Weird that Firebased cloud
36:15 messaging almost always comes up. Not my
36:18 favorite, but it's a solution that
36:19 works. Claude is slightly more likely to
36:21 DIY. Checks out. And I got one last
36:23 thing I want to say before I wrap up.
36:25 It's a short article from friend of the
36:26 channel, Simon Willis. perhaps not
36:28 boring technology after all. A recurring
36:30 concern I've seen regarding LMS for
36:32 programming is that they will push our
36:33 tech choices towards the tools that are
36:35 best represented in their training data,
36:36 making it harder for new and better
36:38 tools to break through the noise. That
36:39 was the case a couple of years ago when
36:40 asking models to help with Python or JS
36:42 appeared to give much better results
36:44 than questions about less widely used
36:45 languages. But with the latest models
36:47 running in good coding agent harnesses,
36:48 I'm not sure that continues to hold up.
36:50 I'm seeing excellent results with my
36:52 brand new tools where I start by
36:53 prompting use uvx showboat-help or
36:56 rodney-help chart room yada yada to
36:58 learn about these tools. The context
37:00 length of these new models is long
37:01 enough that they can consume quite a lot
37:03 of documentation before they start
37:04 working on a problem. Drop a coding
37:05 agent into any existing codebase that
37:07 uses libraries and tools that are too
37:08 private or too new to feature in the
37:10 training data. My experience is that it
37:12 works just fine. The agent will consult
37:13 enough of the existing examples to
37:15 understand patterns and then iterate and
37:16 test its own output to fill in the gaps.
37:18 This has been my experience as well. I
37:21 am seeing the models getting better and
37:22 better and if you combine that with
37:24 tools like skills, it can help even
37:25 more. I'll also call out that if you
37:27 make a lot of different projects like I
37:29 do, you might find it worthwhile to
37:31 modify your Claude MD to include some of
37:33 your specific preferences. So, I have a
37:36 universal clamd in mycloud that
37:38 specifies I like using TypeScript and it
37:39 should never use any unless entirely
37:41 necessary. Commands I don't want to run.
37:43 I hate when my like agents run dev
37:46 servers because I'm already running my
37:47 dev server. [ __ ] touch it. Don't run
37:48 builds unless I ask you to because it'll
37:50 override [ __ ] And use checking commands
37:52 primarily. And for package managers, I
37:53 say use pmpp if it's already using it.
37:55 Otherwise, use bun. Never use npm or
37:57 yarn. I'm going to change this to I'll
37:58 leave it as bun for the default just cuz
38:00 it's quick to install things slightly
38:02 more so than pnpm even if it has
38:03 problems at scale. Text stack
38:05 preferences when uncertain prefer
38:06 tailwind typescript bun react convex
38:08 clerk for cell. This has allowed the
38:10 model to usually get what I want very
38:12 quickly without being steered which is
38:13 very nice. Code style be concise yada
38:16 yada. and then all of the GStack [ __ ]
38:19 from when I was testing out GStack.
38:21 Ignore that. You get the idea, though.
38:22 These models are more willing to
38:24 recommend new [ __ ] than I ever would
38:26 have guessed. And you can always steer
38:27 the model yourself with a little update
38:29 to your MD files to keep it going where
38:32 you want it to go. I have been honestly
38:34 pretty surprised with all of this and I
38:36 am pumped that I found this article.
38:38 Shout out to Edwin for his work on
38:39 amplifying AI. It's a really cool source
38:41 and I had a ton of fun going through
38:43 this. Shout out to him for all the hard
38:44 work. This was a very fun thing to dive
38:46 into. I'm curious how y'all feel about
38:48 these recommendations. Are you more or
38:50 less scared now that you've seen what
38:51 the models actually recommend? I'm
38:53 feeling a little more hopeful, but I'm
38:54 curious if you guys agree. Let me know
38:55 what you think. And until next time,
38:57 peace nerds.
```
