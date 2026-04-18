-- 1. Create the research_sessions table (Updated for better structure)
CREATE TABLE IF NOT EXISTS public.conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL DEFAULT 'New Research',
    query TEXT NOT NULL,
    report TEXT NOT NULL,
    
    -- Added fields to match your README "Output Includes" section
    sources JSONB DEFAULT '[]'::jsonb,
    follow_up_questions JSONB DEFAULT '[]'::jsonb,
    expanded_topics JSONB DEFAULT '[]'::jsonb,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    timestamp BIGINT DEFAULT (extract(epoch from now()) * 1000)::BIGINT -- Matches Date.now() in your React app
);

-- 2. Enable Row Level Security (RLS)
ALTER TABLE public.conversations ENABLE ROW LEVEL SECURITY;

-- 3. Create RLS Policies
CREATE POLICY "Users can view their own conversations" 
ON public.conversations FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own conversations" 
ON public.conversations FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete their own conversations" 
ON public.conversations FOR DELETE USING (auth.uid() = user_id);

-- 4. Performance Indexes
CREATE INDEX IF NOT EXISTS conversations_user_id_idx ON public.conversations (user_id);
CREATE INDEX IF NOT EXISTS conversations_created_at_idx ON public.conversations (created_at DESC);