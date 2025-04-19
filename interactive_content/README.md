# Onchain Edge Interactive Content System

This directory contains the interactive content creation system for Onchain Edge. The system follows a data-driven approach to content creation:

1. **Poll Suggestions** → 2. **Content Creation** → 3. **Performance Tracking** → 4. **Iteration**

## Directory Structure

- **`/polls/`** - Poll suggestions and results
- **`/threads/`** - Thread content based on poll results
- **`/newsletters/`** - Deep dive newsletter content
- **`/metrics/`** - Performance tracking data
- **`/templates/`** - Reusable content templates

## Workflow

1. **Poll Creation**
   - Review poll suggestions in `/polls/suggestions/`
   - Create and post a poll on Twitter
   - Record poll results in `/polls/results/`

2. **Content Development**
   - Use poll results to guide thread creation
   - Create thread content in `/threads/`
   - Develop deeper newsletter content in `/newsletters/`

3. **Performance Tracking**
   - Record performance metrics in `/metrics/`
   - Analyze what worked and what didn't

4. **Iteration**
   - Use insights to improve future content
   - Update content strategy based on performance

## Getting Started

1. Check `/polls/suggestions/` for new poll ideas
2. After running a poll, record results in `/polls/results/`
3. Create content based on poll results
4. Track performance in `/metrics/`
5. Repeat the process with improvements
