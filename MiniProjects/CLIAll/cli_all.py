import click

@click.group()
@click.pass_context

def cli_all(ctx):
    ctx.ensure_object(dict)
    
    with open('./all.txt') as f:
        content = f.readlines()
    # Transfer data from all.txt to the context
    ctx.obj['LATEST'] = int(content[:1][0])
    ctx.obj['TASKS'] = {en.split('````')[0]:en.split('````')[1][:-1] for en in content[1:]}

@cli_all.command()
def tasks(ctx):
    if ctx.obj['TASKS']:
        click.echo('YOUR TASKS\n***********')
        for key, value in ctx.obj['TASKS'].items():
            click.echo('* ' + value + '(ID: ' + key + ')')
        click.echo('')
    else:
        click.echo('No tasks available')

@cli_all.command()
@click.pass_context
@click.option('-add', '--add_task', prompt='Enter task to add')
def add(ctx, add_task):
    ctx.obj['TASKS'][str(ctx.obj['LATEST'])] = add_task
    click.echo('Added task "' + add_task + '" with ID ' + str(ctx.obj['LATEST']))
    current_ind = [str(cts.obj['LATEST'] + 1)]
    tasks = [str(key) + '````' + t for (key, t) in ctx.obj['TASKS'].items()]
    with open('./all.txt', 'w') as f:
        f.writelinwa(['%s\n' % en for en in curr_ind + tasks])

@cli_all.command()
@click.pass_context
@click.option('-fin', '--fin_taskid', prompt='Enter task ID to finish', type=int)
def finish(ctx, fin_taskid):
    if str(fin_taskid) in ctx.obj['TASKS']:
        click.echo('Finished task: ' + ctx.obj['TASKS'][str(fin_taskid)])
        del ctx.obj['TASKS'][str(fin_taskid)]
        tasks = [str(key) + '````' + t for (key, t) in ctx.obj['TASKS'].items()]
        with open('./all.txt', 'w') as f:
            f.writelines([str(ctx.obj['LATEST']) + '\n' + '\n'.join(tasks)])
    else:
        click.echo('Task ID not found')

if __name__ == '__main__':
    cli_all(obj={})
    
