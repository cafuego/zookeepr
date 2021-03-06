<%inherit file="/base.mako" />

<h1>Review ${ c.review.id }</h1>

<h2>#${ c.review.proposal.id } - "${ c.review.proposal.title }"</h2>

<p>
<b>Review by:</b> ${ c.review.reviewer.firstname } ${ c.review.reviewer.lastname }
</p>

<p>
<b>Proposal Abstract:</b>  (${ h.link_to('go to this proposal', url=h.url_for(controller='proposal', action='review', id=c.review.proposal.id)) })
</p>
<blockquote>
<p>${ h.truncate(c.review.proposal.abstract, 200) | h}</p>
</blockquote>

<br />
<p><b>Score:</b> ${ c.review.score | h }</p>
<p><b>Recommended Stream:</b>
% if c.review.stream is not None:
${ c.review.stream.name | h }
% else:
(none)
% endif
</p>
% if c.review.proposal.proposal_type_id is not 2:
<p><b>Recommended Miniconf:</b> ${ c.review.miniconf | h }</p>
% endif

<p><b>Reviewer Comment:</b></p>
<blockquote>
<p>${ c.review.comment | h}</p>
</blockquote>

${ h.link_to('Edit', url=h.url_for(action='edit')) } - ${ h.link_to('Delete', url=h.url_for(action='delete')) }

