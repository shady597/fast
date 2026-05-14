import React, { useState, useEffect } from 'react';
import { api } from './api';
import { PlusCircle, Send, Loader2, RefreshCw } from 'lucide-react';

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isConnected, setIsConnected] = useState(false);
  const [isFetching, setIsFetching] = useState(true);

  const fetchPosts = async () => {
    try {
      setIsFetching(true);
      const data = await api.getPosts();
      setPosts(data);
    } catch (err) {
      console.error(err);
    } finally {
      setIsFetching(false);
    }
  };

  const checkConnection = async () => {
    const ok = await api.checkHealth();
    setIsConnected(ok);
  };

  useEffect(() => {
    fetchPosts();
    checkConnection();
    const interval = setInterval(checkConnection, 10000);
    return () => clearInterval(interval);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !content) return;

    try {
      setIsLoading(true);
      await api.createPost({ title, content });
      setTitle('');
      setContent('');
      await fetchPosts();
    } catch (err) {
      alert('Failed to create post');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>My Blog</h1>
        <div className="status-badge">
          <div className={`status-dot ${isConnected ? 'connected' : ''}`} />
          {isConnected ? 'Connected' : 'Disconnected'}
        </div>
      </header>

      <div className="card post-form">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input 
              type="text" 
              value={title} 
              onChange={(e) => setTitle(e.target.value)} 
              placeholder="What's on your mind?"
              required
            />
          </div>
          <div className="form-group">
            <label>Content</label>
            <textarea 
              value={content} 
              onChange={(e) => setContent(e.target.value)} 
              placeholder="Tell your story..."
              rows="4"
              required
            />
          </div>
          <button type="submit" disabled={isLoading || !isConnected}>
            {isLoading ? <Loader2 className="animate-spin" /> : <Send size={18} />}
            {isLoading ? 'Posting...' : 'Create Post'}
          </button>
        </form>
      </div>

      <div className="post-list">
        <div className="section-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
          <h2>Recent Posts</h2>
          <button className="icon-btn" onClick={fetchPosts} disabled={isFetching} style={{ padding: '0.5rem', background: 'none', color: 'var(--secondary-text)' }}>
            <RefreshCw size={18} className={isFetching ? 'animate-spin' : ''} />
          </button>
        </div>
        
        {isFetching && posts.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '2rem' }}>
            <Loader2 className="animate-spin" style={{ margin: '0 auto' }} />
          </div>
        ) : posts.length === 0 ? (
          <div className="card" style={{ textAlign: 'center', color: 'var(--secondary-text)' }}>
            No posts found. Start by creating one!
          </div>
        ) : (
          posts.map(post => (
            <div key={post.id} className="card post-card">
              <h2>{post.title}</h2>
              <p>{post.content}</p>
              <span className="meta">ID: {post.id.substring(0, 8)}...</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
