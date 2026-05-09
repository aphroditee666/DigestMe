import pytest
from unittest.mock import Mock, patch, MagicMock
from types import SimpleNamespace
from src.rss_fetcher import RSSFetcher, Article

def test_fetch_single_source():
    mock_entries = [
        SimpleNamespace(
            title='Test Article 1',
            link='https://example.com/article1',
            published='Mon, 01 Jan 2026 10:00:00 GMT'
        ),
        SimpleNamespace(
            title='Test Article 2',
            link='https://example.com/article2',
            published='Sun, 31 Dec 2025 10:00:00 GMT'
        )
    ]
    mock_feed = SimpleNamespace(entries=mock_entries)

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss', limit=10)

    assert len(articles) == 2
    assert articles[0].title == 'Test Article 1'
    assert articles[0].url == 'https://example.com/article1'
    assert articles[0].source == '测试号'
    mock_parse.assert_called_once_with('https://example.com/rss')

def test_fetch_with_limit():
    mock_entries = [
        SimpleNamespace(title=f'Article {i}', link=f'https://example.com/{i}', published='Mon, 01 Jan 2026 10:00:00 GMT')
        for i in range(20)
    ]
    mock_feed = SimpleNamespace(entries=mock_entries)

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss', limit=5)

    assert len(articles) == 5

def test_fetch_empty_feed():
    mock_feed = SimpleNamespace(entries=[])

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        fetcher = RSSFetcher()
        articles = fetcher.fetch('测试号', 'https://example.com/rss')

    assert len(articles) == 0


def test_fetch_extracts_content_value_first():
    mock_entry = SimpleNamespace(
        title='Article',
        link='https://example.com/article',
        published='Mon, 01 Jan 2026 10:00:00 GMT',
        content=[{'value': '<p>Full content</p>'}],
        summary='Summary content',
        description='Description content'
    )
    mock_feed = SimpleNamespace(entries=[mock_entry])

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        article = RSSFetcher().fetch('Source', 'https://example.com/rss')[0]

    assert article.content == '<p>Full content</p>'


def test_fetch_extracts_summary_when_content_missing():
    mock_entry = SimpleNamespace(
        title='Article',
        link='https://example.com/article',
        published='Mon, 01 Jan 2026 10:00:00 GMT',
        summary='Summary content',
        description='Description content'
    )
    mock_feed = SimpleNamespace(entries=[mock_entry])

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        article = RSSFetcher().fetch('Source', 'https://example.com/rss')[0]

    assert article.content == 'Summary content'


def test_fetch_extracts_description_when_summary_missing():
    mock_entry = SimpleNamespace(
        title='Article',
        link='https://example.com/article',
        published='Mon, 01 Jan 2026 10:00:00 GMT',
        description='Description content'
    )
    mock_feed = SimpleNamespace(entries=[mock_entry])

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        article = RSSFetcher().fetch('Source', 'https://example.com/rss')[0]

    assert article.content == 'Description content'


def test_fetch_defaults_content_to_empty_string():
    mock_entry = SimpleNamespace(
        title='Article',
        link='https://example.com/article',
        published='Mon, 01 Jan 2026 10:00:00 GMT'
    )
    mock_feed = SimpleNamespace(entries=[mock_entry])

    with patch('feedparser.parse') as mock_parse:
        mock_parse.return_value = mock_feed
        article = RSSFetcher().fetch('Source', 'https://example.com/rss')[0]

    assert article.content == ''
