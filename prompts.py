"""
prompts.py — Reusable prompt library for marketing & content creation.
Each prompt has a name, category, description, template, and list of variables.
"""

PROMPT_LIBRARY = {

    # ── SOCIAL MEDIA ──────────────────────────────────────────────
    "sm_caption_product": {
        "name": "Product Launch Caption",
        "category": "Social Media",
        "description": "Write an engaging Instagram/LinkedIn caption for a new product launch.",
        "template": (
            "Write an engaging {platform} caption for the launch of {product_name}.\n"
            "Brand tone: {tone}.\n"
            "Key benefit to highlight: {key_benefit}.\n"
            "Target audience: {audience}.\n"
            "Include a strong call-to-action and 5 relevant hashtags."
        ),
        "variables": ["platform", "product_name", "tone", "key_benefit", "audience"],
    },

    "sm_engagement_post": {
        "name": "Engagement Booster Post",
        "category": "Social Media",
        "description": "Create a post designed to spark comments and shares.",
        "template": (
            "Create a {platform} post for a brand in the {industry} industry.\n"
            "Goal: maximise engagement (comments, shares).\n"
            "Topic or theme: {topic}.\n"
            "Tone: {tone}.\n"
            "End with a question that encourages followers to share their opinion."
        ),
        "variables": ["platform", "industry", "topic", "tone"],
    },

    "sm_story_script": {
        "name": "Instagram Story Script",
        "category": "Social Media",
        "description": "Write a 5-slide Instagram story script for a campaign.",
        "template": (
            "Write a 5-slide Instagram Story script for {brand_name} promoting {campaign_topic}.\n"
            "Target audience: {audience}.\n"
            "Tone: {tone}.\n"
            "For each slide, provide: slide number, visual description, and caption text.\n"
            "End with a swipe-up or poll CTA."
        ),
        "variables": ["brand_name", "campaign_topic", "audience", "tone"],
    },

    # ── EMAIL MARKETING ───────────────────────────────────────────
    "email_subject_lines": {
        "name": "Email Subject Line Generator",
        "category": "Email Marketing",
        "description": "Generate 10 high-open-rate subject lines for a campaign.",
        "template": (
            "Generate 10 compelling email subject lines for a {campaign_type} campaign.\n"
            "Product or service: {product}.\n"
            "Target audience: {audience}.\n"
            "Key offer or message: {offer}.\n"
            "Include a mix of: curiosity-driven, urgency-based, benefit-focused, and personalised styles.\n"
            "Keep each subject line under 50 characters."
        ),
        "variables": ["campaign_type", "product", "audience", "offer"],
    },

    "email_welcome": {
        "name": "Welcome Email",
        "category": "Email Marketing",
        "description": "Draft a warm, on-brand welcome email for new subscribers.",
        "template": (
            "Write a welcome email for new subscribers of {brand_name}.\n"
            "Brand tone: {tone}.\n"
            "What the subscriber signed up for: {signup_reason}.\n"
            "One key thing you want them to do next: {cta}.\n"
            "Keep it under 200 words, warm, and human."
        ),
        "variables": ["brand_name", "tone", "signup_reason", "cta"],
    },

    # ── CONTENT STRATEGY ──────────────────────────────────────────
    "content_blog_outline": {
        "name": "Blog Post Outline",
        "category": "Content Strategy",
        "description": "Generate a structured outline for a blog post.",
        "template": (
            "Create a detailed blog post outline on the topic: '{topic}'.\n"
            "Target audience: {audience}.\n"
            "Desired tone: {tone}.\n"
            "Target length: {length} words.\n"
            "Include: a hook introduction, 5–7 main sections with subpoints, and a conclusion with CTA.\n"
            "Also suggest 3 SEO-friendly title options."
        ),
        "variables": ["topic", "audience", "tone", "length"],
    },

    "content_repurpose": {
        "name": "Content Repurposing Plan",
        "category": "Content Strategy",
        "description": "Turn one piece of content into a multi-platform strategy.",
        "template": (
            "I have a {content_type} about '{topic}'.\n"
            "Brand: {brand_name}, Industry: {industry}.\n"
            "Create a repurposing plan to adapt this content for: Instagram, LinkedIn, Twitter/X, a newsletter, and a YouTube short.\n"
            "For each platform, describe: format, key message, and tone adjustments."
        ),
        "variables": ["content_type", "topic", "brand_name", "industry"],
    },

    # ── AD COPY ───────────────────────────────────────────────────
    "ad_google": {
        "name": "Google Ads Copy",
        "category": "Ad Copy",
        "description": "Write Google Search ad headlines and descriptions.",
        "template": (
            "Write Google Search ad copy for {product_or_service}.\n"
            "Target keyword: {keyword}.\n"
            "Unique selling point: {usp}.\n"
            "Target audience: {audience}.\n"
            "Provide: 5 headlines (max 30 chars each) and 2 descriptions (max 90 chars each).\n"
            "Focus on clarity, relevance, and a strong CTA."
        ),
        "variables": ["product_or_service", "keyword", "usp", "audience"],
    },

    "ad_meta": {
        "name": "Meta (Facebook/Instagram) Ad",
        "category": "Ad Copy",
        "description": "Write a complete Meta ad with hook, body, and CTA.",
        "template": (
            "Write a Meta ad for {product_or_service}.\n"
            "Objective: {objective} (e.g. traffic, conversions, awareness).\n"
            "Target audience: {audience}.\n"
            "Tone: {tone}.\n"
            "Provide: attention-grabbing hook (1 line), ad body (3–4 lines), and a CTA button text.\n"
            "Also suggest what the visual/image should show."
        ),
        "variables": ["product_or_service", "objective", "audience", "tone"],
    },

    # ── AI & PRODUCTIVITY ─────────────────────────────────────────
    "ai_system_prompt": {
        "name": "Custom AI System Prompt",
        "category": "AI & Productivity",
        "description": "Design a system prompt to configure an AI assistant for a specific role.",
        "template": (
            "Write a system prompt for an AI assistant that will act as a {role} for {company_type}.\n"
            "The assistant should: {key_behaviours}.\n"
            "It should always avoid: {restrictions}.\n"
            "Tone and communication style: {tone}.\n"
            "Include instructions for handling edge cases and staying on-topic."
        ),
        "variables": ["role", "company_type", "key_behaviours", "restrictions", "tone"],
    },

    "ai_chain_prompt": {
        "name": "Prompt Chain Builder",
        "category": "AI & Productivity",
        "description": "Design a multi-step prompt chain for a complex task.",
        "template": (
            "Design a 4-step prompt chain to accomplish the following goal: {goal}.\n"
            "Context: {context}.\n"
            "For each step provide: Step number, Objective, Exact prompt to use, Expected output format.\n"
            "Make sure each step's output feeds naturally into the next step."
        ),
        "variables": ["goal", "context"],
    },
}
