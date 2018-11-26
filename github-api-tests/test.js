const supertest = require('supertest');
const request = supertest.agent('https://api.github.com');

// ------------------- POSITIVE TESTS -------------------

 describe('GET /users positive tests', function(){
    it('1.1 Should return 200 status for /users', function(done){
      request
      .get('/users')
			.expect('Content-Type', /json/)
      .expect('Content-Encoding', 'gzip')
			.expect(200, done);
		})

  it('1.2 Authenticated user should return non-public data', function(done) {
    request
    .get('/users/jevgarcia22')
    //test will fail without valid token tied to user
    .set('Authorization', 'token 123xyz')
    .expect('Content-Type', /json/)
    .expect(200,
      {
        "login": "jevgarcia22",
        "id": 35239335,
        "node_id": "MDQ6VXNlcjM1MjM5MzM1",
        "avatar_url": "https://avatars2.githubusercontent.com/u/35239335?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jevgarcia22",
        "html_url": "https://github.com/jevgarcia22",
        "followers_url": "https://api.github.com/users/jevgarcia22/followers",
        "following_url": "https://api.github.com/users/jevgarcia22/following{/other_user}",
        "gists_url": "https://api.github.com/users/jevgarcia22/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jevgarcia22/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jevgarcia22/subscriptions",
        "organizations_url": "https://api.github.com/users/jevgarcia22/orgs",
        "repos_url": "https://api.github.com/users/jevgarcia22/repos",
        "events_url": "https://api.github.com/users/jevgarcia22/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jevgarcia22/received_events",
        "type": "User",
        "site_admin": false,
        "name": null,
        "company": null,
        "blog": "",
        "location": null,
        "email": null,
        "hireable": null,
        "bio": null,
        "public_repos": 1,
        "public_gists": 0,
        "followers": 0,
        "following": 0,
        "created_at": "2018-01-08T21:18:48Z",
        "updated_at": "2018-11-19T04:31:54Z",
        "private_gists": 0,
        "total_private_repos": 2,
        "owned_private_repos": 2,
        "disk_usage": 2659,
        "collaborators": 0,
        "two_factor_authentication": false,
        "plan": {
            "name": "developer",
            "space": 976562499,
            "collaborators": 0,
            "private_repos": 9999
        }
      } ,done)
    })
  });


// ------------------- NEGATIVE TESTS -------------------
describe('GET /users negative tests', function(){

	it('2.1 Should return 404 status for invalid user', function(done){
		request
		.get('/users/some-invalid-user')
		.expect('Content-Type', /json/)
		.expect(404,
			{
				message: "Not Found",
				documentation_url: "https://developer.github.com/v3/users/#get-a-single-user"
			}
		, done);
		})

  it('2.2 Non-Authenticated user should not return non-public data', function(done) {
    request
    .get('/users/octocat')
    .expect('Content-Type', /json/)
    .expect(200,
      {
        "login": "octocat",
        "id": 583231,
        "node_id": "MDQ6VXNlcjU4MzIzMQ==",
        "avatar_url": "https://avatars3.githubusercontent.com/u/583231?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false,
        "name": "The Octocat",
        "company": "GitHub",
        "blog": "http://www.github.com/blog",
        "location": "San Francisco",
        "email": null,
        "hireable": null,
        "bio": null,
        "public_repos": 8,
        "public_gists": 8,
        "followers": 2440,
        "following": 9,
        "created_at": "2011-01-25T18:44:36Z",
        "updated_at": "2018-11-06T16:21:16Z"
      }, done)
  })

  it('2.3 Should return 401 for invalid token', function(done) {
    request
    .get('/users/jevgarcia22')
    .set('Authorization', 'token 123xyz')
    .expect('Content-Type', /json/)
    .expect(401, {
      message: "Bad credentials",
      documentation_url: "https://developer.github.com/v3"
    }, done)
  })


});
